from typing import Any, Type, TypeVar

from fastapi import HTTPException
from sqlalchemy.exc import MultipleResultsFound
from sqlmodel import SQLModel, select

from .database import SessionDep

T = TypeVar("T", bound=SQLModel)


def get_or_raise(session: SessionDep, model: Type[T], object_id: int) -> T:
    obj = session.get(model, object_id)
    if not obj:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")

    return obj


def get_or_create(
    session: SessionDep,
    model: Type[T],
    defaults: dict[str, Any] | None = None,
    **kwargs: Any,
) -> tuple[T, bool]:

    conditions = [getattr(model, key) == value for key, value in kwargs.items()]
    statement = select(model).where(*conditions)

    try:
        obj = session.exec(statement).one_or_none()
    except MultipleResultsFound:
        raise HTTPException(
            status_code=400,
            detail=f"Multiple {model.__name__} instances found for the given criteria",
        )

    if obj:
        return obj, False

    kwargs |= defaults or {}
    obj = model(**kwargs)

    try:
        session.add(obj)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

    return obj, True

from typing import Annotated
from fastapi import APIRouter, Query, HTTPException
from sqlmodel import select

from ..models.label import Label, CreateLabel, ReadLabel
from ..database import SessionDep


router = APIRouter(prefix="/labels", tags=["Labels"])


@router.get("/", response_model=list[Label])
def get_all(session: SessionDep):
    return session.exec(select(Label)).all()


@router.get("/{label_id}", response_model=ReadLabel)
def get(label_id: int, session: SessionDep):
    label = session.get(Label, label_id)
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")

    return label


@router.post("/", response_model=ReadLabel, status_code=201)
def create(label: CreateLabel, session: SessionDep):

    db_label = Label(name=label.name, color=label.color)

    session.add(db_label)
    session.commit()
    session.refresh(db_label)

    return db_label


@router.patch("/{label_id}", response_model=ReadLabel)
def update(label_id: int, label: CreateLabel, session: SessionDep):

    db_label = session.get(Label, label_id)
    if not db_label:
        raise HTTPException(status_code=404, detail="Label not found")

    label_data = label.model_dump(exclude_unset=True)
    db_label.sqlmodel_update(label_data)

    session.add(db_label)
    session.commit()
    session.refresh(db_label)

    return db_label


@router.delete("/{label_id}", status_code=204)
def delete(label_id: int, session: SessionDep):
    gift_db = session.get(Label, label_id)
    if not gift_db:
        raise HTTPException(status_code=404, detail="Label not found")

    session.delete(gift_db)
    session.commit()

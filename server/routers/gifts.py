from typing import Annotated

from fastapi import APIRouter, Query, HTTPException
from sqlmodel import select

from ..models.gifts import Gift, GiftBase
from ..database import SessionDep


router = APIRouter(prefix="/gifts", tags=["Gifts"])

@router.get("/", response_model=list[Gift])
def get_all(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(gt=0, le=100)] = 10,
):
    gifts = session.exec(select(Gift).offset(offset).limit(limit)).all()
    return gifts

@router.get("/{gift_id}", response_model=Gift)
def get(gift_id: int, session: SessionDep):
    gift = session.get(Gift, gift_id)
    if not gift:
        raise HTTPException(status_code=404, detail="Gift not found")

    return gift

@router.post("/", response_model=Gift)
def create(gift: GiftBase, session: SessionDep):
    db_gift = Gift.model_validate(gift)
    session.add(db_gift)
    session.commit()
    session.refresh(db_gift)
    return db_gift

@router.patch("/{gift_id}", response_model=Gift)
def update(gift_id: int, gift: GiftBase, session: SessionDep):
    gift_db = session.get(Gift, gift_id)
    if not gift_db:
        raise HTTPException(status_code=404, detail="Gift not found")

    gift_data = gift.model_dump(exclude_unset=True)
    gift_db.sqlmodel_update(gift_data)

    session.add(gift_db)
    session.commit()
    session.refresh(gift_db)

    return gift_db

@router.delete("/{gift_id}")
def delete(gift_id: int, session: SessionDep):
    gift_db = session.get(Gift, gift_id)
    if not gift_db:
        raise HTTPException(status_code=404, detail="Gift not found")

    session.delete(gift_db)
    session.commit()
    return {"ok": True}

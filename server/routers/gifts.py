from typing import List

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from ..models.gift import Gift, CreateGift, ReadGift, PatchGift
from ..models.label import Label
from ..database import SessionDep


router = APIRouter(prefix="/gifts", tags=["Gifts"])


def get_or_create_labels(session: SessionDep, label_names: List[str]) -> List[Label]:

    label_objects: List[Label] = []
    for label_name in set(label_names):
        label_name = label_name.strip()
        if not label_name:
            continue

        qs = select(Label).where(Label.name == label_name)
        existing = session.exec(qs).first()

        if existing:
            label_objects.append(existing)
        else:
            new_label = Label(name=label_name)
            session.add(new_label)
            session.flush()
            label_objects.append(new_label)

    return label_objects


@router.get("/", response_model=list[ReadGift])
def get_all(session: SessionDep):
    return session.exec(select(Gift)).all()


@router.get("/{gift_id}", response_model=ReadGift)
def get(gift_id: int, session: SessionDep):
    gift = session.get(Gift, gift_id)
    if not gift:
        raise HTTPException(status_code=404, detail="Gift not found")

    return gift


@router.post("/", response_model=ReadGift, status_code=201)
def create(gift: CreateGift, session: SessionDep):

    label_objects = get_or_create_labels(session, gift.labels)
    db_gift = Gift(
        name=gift.name,
        description=gift.description,
        url=gift.url,
        labels=label_objects,
    )

    session.add(db_gift)
    session.commit()
    session.refresh(db_gift)

    return db_gift


@router.patch("/{gift_id}", response_model=ReadGift)
def update(gift_id: int, gift: PatchGift, session: SessionDep):

    db_gift = session.get(Gift, gift_id)
    if not db_gift:
        raise HTTPException(status_code=404, detail="Gift not found")

    gift_data = gift.model_dump(exclude_unset=True)
    label_names = gift_data.pop("labels", [])

    db_gift.sqlmodel_update(gift_data)
    db_gift.labels = get_or_create_labels(session, label_names)

    session.add(db_gift)
    session.commit()
    session.refresh(db_gift)

    return db_gift


@router.delete("/{gift_id}", status_code=204)
def delete(gift_id: int, session: SessionDep):
    gift_db = session.get(Gift, gift_id)
    if not gift_db:
        raise HTTPException(status_code=404, detail="Gift not found")

    session.delete(gift_db)
    session.commit()

from typing import List

from fastapi import APIRouter
from sqlmodel import select

from . import helpers, models
from .database import SessionDep as session

gifts = APIRouter(prefix="/gifts", tags=["Gifts"])
labels = APIRouter(prefix="/labels", tags=["Labels"])
people = APIRouter(prefix="/people", tags=["People"])


@gifts.get("/", response_model=List[models.ReadGift])
def get_gifts(session: session):
    return session.exec(select(models.Gift)).all()


@gifts.get("/{gift_id}", response_model=models.ReadGift)
def get_gift(gift_id: int, session: session):
    return helpers.get_or_raise(session, models.Gift, gift_id)


@gifts.post("/", response_model=models.ReadGift, status_code=201)
def create_gift(gift: models.CreateGift, session: session):
    label_objects = []
    for label_id in gift.labels:
        label = helpers.get_or_raise(session, models.Label, label_id)
        label_objects.append(label)

    gift_data = gift.model_dump(exclude={"labels"})
    db_gift = models.Gift.model_validate(gift_data)
    db_gift.labels = label_objects

    session.add(db_gift)
    session.commit()

    return db_gift


@gifts.patch("/{gift_id}", response_model=models.ReadGift)
def update_gift(gift_id: int, gift: models.PatchGift, session: session):
    db_gift = helpers.get_or_raise(session, models.Gift, gift_id)
    gift_data = gift.model_dump(exclude_unset=True)

    label_objects = []
    for label_id in gift.labels:
        label = helpers.get_or_raise(session, models.Label, label_id)
        label_objects.append(label)

    db_gift.sqlmodel_update(gift_data)
    db_gift.labels = label_objects

    session.add(db_gift)
    session.commit()
    session.refresh(db_gift)

    return db_gift


@gifts.delete("/{gift_id}", status_code=204)
def delete_gift(gift_id: int, session: session):
    db_gift = helpers.get_or_raise(session, models.Gift, gift_id)
    session.delete(db_gift)
    session.commit()


@labels.get("/", response_model=List[models.ReadLabel])
def get_labels(session: session):
    return session.exec(select(models.Label)).all()


@labels.get("/{label_id}", response_model=models.ReadLabel)
def get_label(label_id: int, session: session):
    return helpers.get_or_raise(session, models.Label, label_id)


@labels.post("/", response_model=models.ReadLabel, status_code=201)
def create_label(label: models.CreateLabel, session: session):
    db_label = models.Label.model_validate(label)
    session.add(db_label)
    session.commit()
    return db_label


@labels.patch("/{label_id}", response_model=models.ReadLabel)
def update_label(label_id: int, label: models.PatchLabel, session: session):
    db_label = helpers.get_or_raise(session, models.Label, label_id)
    label_data = label.model_dump(exclude_unset=True)
    db_label.sqlmodel_update(label_data)

    session.add(db_label)
    session.commit()
    session.refresh(db_label)

    return db_label


@labels.delete("/{label_id}", status_code=204)
def delete_label(label_id: int, session: session):
    db_label = helpers.get_or_raise(session, models.Label, label_id)
    session.delete(db_label)
    session.commit()


@people.get("/", response_model=List[models.ReadPerson])
def get_people(session: session):
    return session.exec(select(models.Person)).all()


@people.get("/{person_id}", response_model=models.ReadPerson)
def get_person(person_id: int, session: session):
    return helpers.get_or_raise(session, models.Person, person_id)


@people.post("/", response_model=models.ReadPerson, status_code=201)
def create_person(person: models.CreatePerson, session: session):
    db_person = models.Person.model_validate(person)
    session.add(db_person)
    session.commit()
    session.refresh(db_person)
    return db_person


@people.patch("/{person_id}", response_model=models.ReadPerson)
def update_person(person_id: int, person: models.PatchPerson, session: session):
    db_person = helpers.get_or_raise(session, models.Person, person_id)
    data = person.model_dump(exclude_unset=True)
    db_person.sqlmodel_update(data)

    session.add(db_person)
    session.commit()
    session.refresh(db_person)

    return db_person


@people.delete("/{person_id}", status_code=204)
def delete_person(person_id: int, session: session):
    db_person = helpers.get_or_raise(session, models.Person, person_id)
    session.delete(db_person)
    session.commit()


@people.post("/{person_id}/gifts/", status_code=204)
def add_gift_to_person(person_id: int, gift_id: int, session: session):
    person = helpers.get_or_raise(session, models.Person, person_id)
    gift = helpers.get_or_raise(session, models.Gift, gift_id)

    if gift not in person.gifts:
        person.gifts.append(gift)
        session.add(person)
        session.commit()

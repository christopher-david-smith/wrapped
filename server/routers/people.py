from typing import List

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from ..models.person import Person, CreatePerson, ReadPerson, PatchPerson
from ..database import SessionDep

router = APIRouter(prefix="/people", tags=["People"])


@router.post("/", response_model=Person, status_code=201)
def create(person: CreatePerson, session: SessionDep):
    db_person = Person(
        name=person.name,
        date_of_birth=person.date_of_birth,
        include_in_christmas=person.include_in_christmas,
    )

    session.add(db_person)
    session.commit()
    session.refresh(db_person)

    return db_person


@router.get("/", response_model=List[ReadPerson])
def get_all(session: SessionDep):
    return session.exec(select(Person)).all()


@router.get("/{person_id}", response_model=ReadPerson)
def get(person_id: int, session: SessionDep):
    person = session.get(Person, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    return person


@router.patch("/{person_id}")
def update():
    pass


@router.delete("/{person_id}")
def delete():
    pass


@router.post("/{person_id}/gift")
def add_gift():
    pass


@router.delete("/{person_id}/gift")
def delete_gift():
    pass


@router.patch("/{person_id}/gift/{gift_id}")
def update_gift():
    pass

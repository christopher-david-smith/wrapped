from typing import TYPE_CHECKING, List
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from ..models.gift import ReadGift

if TYPE_CHECKING:
    from .gift import Gift


class PersonBase(SQLModel):
    name: str = Field(index=True)
    date_of_birth: datetime
    include_in_christmas: bool = False


class Person(PersonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    gifts: List["Gift"] = Relationship(back_populates="person")


class CreatePerson(PersonBase):
    pass


class ReadPerson(PersonBase):
    id: int
    gifts: List[ReadGift] = []


class PatchPerson(PersonBase):
    id: int

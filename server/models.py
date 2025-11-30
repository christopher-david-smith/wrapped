import random
import re
from datetime import date
from typing import TYPE_CHECKING, List, Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel

HEX_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}$")


def random_color() -> str:
    return "#%06X" % random.randint(0, 0xFFFFFF)


class GiftLabelLink(SQLModel, table=True):
    gift_id: int = Field(foreign_key="gift.id", primary_key=True)
    label_id: int = Field(foreign_key="label.id", primary_key=True)


class GiftBase(SQLModel):
    name: str = Field(index=True)
    description: str | None = None
    url: str | None = None


class Gift(GiftBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    labels: List["Label"] = Relationship(
        back_populates="gifts", link_model=GiftLabelLink
    )

    recipient_id: int | None = Field(default=None, foreign_key="person.id")
    person: Optional["Person"] = Relationship(back_populates="gifts")


class CreateGift(GiftBase):
    labels: List[int] = []
    recipient_id: int | None = None


class ReadGift(GiftBase):
    id: int
    labels: List["ReadLabel"] = []


class PatchGift(GiftBase):
    labels: List[int] = []


class LabelBase(SQLModel):
    name: str = Field(index=True)
    color: str | None = Field(default_factory=random_color)

    @field_validator("color", mode="before")
    @classmethod
    def ensure_valid_color(cls, value: str) -> str:
        if not value:
            return random_color()

        if not HEX_PATTERN.match(value):
            raise ValueError("Color must be a valid hex code")

        return value


class Label(LabelBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    gifts: List["Gift"] = Relationship(
        back_populates="labels", link_model=GiftLabelLink
    )


class ReadLabel(LabelBase):
    id: int


class CreateLabel(LabelBase):
    pass


class PatchLabel(LabelBase):
    pass


class PersonBase(SQLModel):
    name: str = Field(index=True)
    date_of_birth: date
    include_in_christmas: bool = False


class Person(PersonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    gifts: List["Gift"] = Relationship(back_populates="person")


class CreatePerson(PersonBase):
    pass


class ReadPerson(PersonBase):
    id: int
    gifts: List["ReadGift"] = []


class PatchPerson(SQLModel):
    name: str | None = None
    date_of_birth: date | None = None
    include_in_christmas: bool | None = None

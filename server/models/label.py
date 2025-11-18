import random
from typing import TYPE_CHECKING, List

from sqlmodel import SQLModel, Relationship, Field

from .relationships import GiftLabelLink

if TYPE_CHECKING:
    from .gift import Gift


def random_color() -> str:
    return "#%06X" % random.randint(0, 0xFFFFFF)


class LabelBase(SQLModel):
    name: str = Field(index=True)
    color: str | None = Field(default_factory=random_color)


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

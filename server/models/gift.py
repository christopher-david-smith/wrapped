from typing import TYPE_CHECKING, List, Optional
from datetime import datetime

from sqlmodel import Field, SQLModel, Relationship

from .label import ReadLabel
from .relationships import GiftLabelLink

if TYPE_CHECKING:
    from .label import Label
    from .person import Person


class GiftBase(SQLModel):
    name: str = Field(index=True)
    description: str | None = None
    url: str | None = None


class Gift(GiftBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)

    labels: List["Label"] = Relationship(
        back_populates="gifts", link_model=GiftLabelLink
    )

    recipient_id: int | None = Field(
        default=None,
        foreign_key="person.id",
    )

    person: Optional["Person"] = Relationship(back_populates="gifts")


class CreateGift(GiftBase):
    labels: List[str] = []


class ReadGift(GiftBase):
    id: int
    created: datetime
    labels: List[ReadLabel] = []


class PatchGift(GiftBase):
    pass

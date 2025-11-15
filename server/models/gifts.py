from datetime import datetime

from sqlmodel import Field, SQLModel


class GiftBase(SQLModel):
    name: str = Field(index=True)
    description: str | None = Field(default=None)

class Gift(GiftBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)

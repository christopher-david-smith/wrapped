from sqlmodel import SQLModel, Field


class GiftLabelLink(SQLModel, table=True):
    gift_id: int = Field(foreign_key="gift.id", primary_key=True)
    label_id: int = Field(foreign_key="label.id", primary_key=True)

from datetime import datetime

import sqlalchemy.orm as so
from sqlalchemy import TIMESTAMP, func

from src.core.models import Base
from src.core.schemas import User as UserSchema


class User(Base):
    __tablename__ = "users"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, index=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    surname: so.Mapped[str] = so.mapped_column(nullable=False)
    password: so.Mapped[str] = so.mapped_column(nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: so.Mapped[datetime] = so.mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def to_pydantic_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            surname=self.surname,
            password=self.password,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

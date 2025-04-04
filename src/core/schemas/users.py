from datetime import datetime

from pydantic import BaseModel, PositiveInt


class UserBase(BaseModel):
    name: str
    surname: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDB(UserBase):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class User(UserInDB):
    pass

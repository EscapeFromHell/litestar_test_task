from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.core.models import User
from src.core.repository.repository import SqlAlchemyRepository
from src.core.schemas import UserCreate, UserUpdate


class UsersRepository(SqlAlchemyRepository):
    model = User

    async def create_user(self, user: UserCreate) -> User:
        user_model = self.model(name=user.name, surname=user.surname, password=user.password)
        self.session.add(user_model)
        return user_model

    async def get_users(self) -> Sequence[User]:
        query = await self.session.execute(select(self.model))
        return query.scalars().all()

    async def get_user(self, user_id: int) -> User | None:
        try:
            query = await self.session.execute(select(self.model).filter_by(id=user_id))
            db_user = query.scalars().one()

        except NoResultFound:
            return None

        else:
            return db_user

    async def update_user(self, user_id: int, user: UserUpdate) -> User | None:
        try:
            query = await self.session.execute(select(self.model).filter_by(id=user_id))
            db_user = query.scalars().one()
            for key, value in user.model_dump().items():
                setattr(db_user, key, value)

        except NoResultFound:
            return None

        else:
            return db_user

    async def delete_user(self, user_id: int) -> dict | None:
        try:
            query = await self.session.execute(select(self.model).filter_by(id=user_id))
            db_user = query.scalars().one()
            await self.session.delete(db_user)

        except NoResultFound:
            return None

        else:
            return {"message": f"User with id: {user_id} deleted"}

from litestar.exceptions import HTTPException

from src.core.schemas import User, UserCreate, UserUpdate
from src.core.service.service import BaseService
from src.core.uow import UnitOfWork


class UsersService(BaseService):
    base_repository: str = "users"

    @classmethod
    async def create_user(cls, user: UserCreate, uow: UnitOfWork) -> User:
        async with uow:
            result = await uow.__dict__[cls.base_repository].create_user(user=user)
        created_user = result.to_pydantic_schema()
        return created_user

    @classmethod
    async def get_users(cls, uow: UnitOfWork) -> list[User]:
        async with uow:
            result = await uow.__dict__[cls.base_repository].get_users()
        users = [user.to_pydantic_schema() for user in result]
        return users

    @classmethod
    async def get_user(cls, user_id: int, uow: UnitOfWork) -> User:
        async with uow:
            result = await uow.__dict__[cls.base_repository].get_user(user_id=user_id)
        if not result:
            raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")
        user = result.to_pydantic_schema()
        return user

    @classmethod
    async def update_user(cls, user_id: int, user: UserUpdate, uow: UnitOfWork) -> User:
        async with uow:
            result = await uow.__dict__[cls.base_repository].update_user(user_id=user_id, user=user)
        if not result:
            raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")
        updated_user = result.to_pydantic_schema()
        return updated_user

    @classmethod
    async def delete_user(cls, user_id: int, uow: UnitOfWork) -> dict:
        async with uow:
            result = await uow.__dict__[cls.base_repository].delete_user(user_id=user_id)
        if not result:
            raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")
        return result

from litestar import Router, delete, get, post, put
from litestar.di import Provide
from litestar.params import Dependency

from src.core.schemas import User, UserCreate, UserUpdate
from src.core.service import UsersService
from src.core.uow import UnitOfWork


@post("/", status_code=201, dependencies={"uow": Provide(UnitOfWork, sync_to_thread=False)})
async def create_user(data: UserCreate, uow: UnitOfWork = Dependency()) -> User:
    return await UsersService.create_user(user=data, uow=uow)


@get("/", status_code=200, dependencies={"uow": Provide(UnitOfWork, sync_to_thread=False)})
async def get_users(uow: UnitOfWork = Dependency()) -> list[User]:
    return await UsersService.get_users(uow=uow)


@get("/{user_id:int}", status_code=200, dependencies={"uow": Provide(UnitOfWork, sync_to_thread=False)})
async def get_user(user_id: int, uow: UnitOfWork = Dependency()) -> User:
    return await UsersService.get_user(user_id=user_id, uow=uow)


@put("/{user_id:int}", status_code=200, dependencies={"uow": Provide(UnitOfWork, sync_to_thread=False)})
async def update_user(user_id: int, data: UserUpdate, uow: UnitOfWork = Dependency()) -> User:
    return await UsersService.update_user(user_id=user_id, user=data, uow=uow)


@delete("/{user_id:int}", status_code=200, dependencies={"uow": Provide(UnitOfWork, sync_to_thread=False)})
async def delete_user(user_id: int, uow: UnitOfWork = Dependency()) -> dict:
    return await UsersService.delete_user(user_id=user_id, uow=uow)


router = Router(path="/users", route_handlers=[create_user, get_users, get_user, update_user, delete_user])

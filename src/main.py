import uvicorn
from advanced_alchemy.extensions.litestar.plugins import SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin
from litestar import Litestar

from src.api.api_v1.endpoints import router
from src.config import settings

config = SQLAlchemyAsyncConfig(connection_string=settings.DB_URL)
plugin = SQLAlchemyInitPlugin(config)


def get_application() -> Litestar:
    app = Litestar(route_handlers=[router], plugins=[plugin])
    return app


app = get_application()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, log_level="info")

from fastapi import FastAPI

from src.apps.webhooks.container import Container
from src.apps.webhooks.routers import notifications

container = Container()

app = FastAPI()
app.container = container  # type: ignore
app.include_router(notifications.router)

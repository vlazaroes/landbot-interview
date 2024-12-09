from fastapi import FastAPI

from apps.webhooks.container import Container
from apps.webhooks.routers import notifications

container = Container()

app = FastAPI()
app.container = container
app.include_router(notifications.router)

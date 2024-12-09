from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from apps.webhooks.container import Container
from apps.webhooks.schemas.notification import Notification
from contexts.notifications.application.create.notification_creator import (
    NotificationCreator,
)

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])


@router.post("/notification", status_code=status.HTTP_204_NO_CONTENT)
@inject
def send_notification(
    notification: Notification,
    notification_creator: NotificationCreator = Depends(
        Provide[Container.notification_creator]
    ),
) -> None:
    notification_creator.run(notification.topic, notification.description)
    return None

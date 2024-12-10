from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

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
    try:
        notification_creator.run(notification.topic, notification.description)
        return None
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
        ) from error
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        ) from error

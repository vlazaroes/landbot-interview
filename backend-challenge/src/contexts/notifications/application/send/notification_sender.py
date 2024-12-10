import uuid

from src.contexts.notifications.domain.notification import Notification
from src.contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from src.contexts.notifications.domain.notification_id import NotificationId
from src.contexts.notifications.domain.notification_topic import NotificationTopic
from src.contexts.notifications.domain.notifier import Notifier


class NotificationSender:
    def __init__(self, notifier: Notifier) -> None:
        self.__notifier = notifier

    def run(self, id: str, topic: str, description: str) -> None:
        notification = Notification(
            id=NotificationId(value=uuid.UUID(id)),
            topic=NotificationTopic(value=topic),
            description=NotificationDescription(value=description),
        )
        self.__notifier.notify(notification)

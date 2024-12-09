from contexts.notifications.domain.notification import Notification
from contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from contexts.notifications.domain.notification_id import NotificationId
from contexts.notifications.domain.notification_topic import NotificationTopic
from contexts.notifications.domain.notifier import Notifier


class NotificationSender:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def run(self, id: str, topic: str, description: str) -> None:
        notification = Notification(
            id=NotificationId(value=id),
            topic=NotificationTopic(value=topic),
            description=NotificationDescription(value=description),
        )
        self.notifier.notify(notification)

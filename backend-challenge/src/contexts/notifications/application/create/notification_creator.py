import uuid

from contexts.notifications.domain.notification import Notification
from contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from contexts.notifications.domain.notification_id import NotificationId
from contexts.notifications.domain.notification_topic import NotificationTopic
from contexts.shared.domain.events.event_bus import EventBus


class NotificationCreator:
    def __init__(self, event_bus: EventBus) -> None:
        self.__event_bus = event_bus

    def run(self, topic: str, description: str) -> None:
        notification = Notification.create(
            id=NotificationId(value=uuid.uuid4()),
            topic=NotificationTopic(value=topic),
            description=NotificationDescription(value=description),
        )
        self.__event_bus.publish_domain_events(notification.pull_domain_events())

import json
from abc import ABC

from src.contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from src.contexts.notifications.domain.notification_id import NotificationId
from src.contexts.notifications.domain.notification_topic import NotificationTopic
from src.contexts.shared.domain.events.domain_event import DomainEvent


class NotificationCreatedDomainEvent(DomainEvent, ABC):
    id: NotificationId
    topic: NotificationTopic
    description: NotificationDescription

    def serialize(self) -> str:
        return json.dumps(
            {
                "data": {
                    "id": self.get_event_id(),
                    "type": self.get_event_name(),
                    "ocurred_on": self.get_ocurred_on(),
                    "attributes": {
                        "id": str(self.id.value),
                        "topic": self.topic.value,
                        "description": self.description.value,
                    },
                    "meta": [],
                },
            }
        )

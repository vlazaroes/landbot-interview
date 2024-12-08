import json
from abc import ABC

from pydantic import BaseModel

from contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from contexts.notifications.domain.notification_id import NotificationId
from contexts.notifications.domain.notification_topic import NotificationTopic
from contexts.shared.domain.events.domain_event import DomainEvent


class NotificationCreatedDomainEvent(DomainEvent, BaseModel, ABC):
    id: NotificationId
    topic: NotificationTopic
    description: NotificationDescription

    def serialize(self) -> str:
        return json.dumps(
            {
                "data": {
                    "id": str(self.event_id.value),
                    "type": self.get_event_name(),
                    "ocurred_on": str(self.ocurred_on),
                    "attributes": {
                        "id": str(self.id.value),
                        "topic": self.topic.value,
                        "description": self.description.value,
                    },
                    "meta": [],
                },
            }
        )

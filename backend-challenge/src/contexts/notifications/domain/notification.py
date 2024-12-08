from typing import Any, Optional

from contexts.notifications.domain.events.notification_email_created_domain_event import (
    NotificationEmailCreatedDomainEvent,
)
from contexts.notifications.domain.events.notification_slack_created_domain_event import (
    NotificationSlackCreatedDomainEvent,
)
from contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from contexts.notifications.domain.notification_id import NotificationId
from contexts.notifications.domain.notification_topic import NotificationTopic
from contexts.shared.domain.aggregates.aggregate_root import AggregateRoot


class Notification(AggregateRoot):
    id: NotificationId
    topic: NotificationTopic
    description: NotificationDescription

    @staticmethod
    def create(
        id: NotificationId,
        topic: NotificationTopic,
        description: NotificationDescription,
    ) -> "Notification":
        notification = Notification(id=id, topic=topic, description=description)
        created_domain_event_class = Notification.__get_created_domain_event(
            topic=topic
        )
        if not created_domain_event_class:
            raise ValueError("The topic value is invalid")
        notification.record_domain_event(
            created_domain_event_class(topic=topic, description=description)
        )
        return notification

    @staticmethod
    def __get_created_domain_event(topic: NotificationTopic) -> Optional[Any]:
        CREATED_DOMAIN_EVENTS = {
            "SLACK": NotificationSlackCreatedDomainEvent,
            "EMAIL": NotificationEmailCreatedDomainEvent,
        }
        return CREATED_DOMAIN_EVENTS.get(topic.value.upper(), None)

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
        notification.record_created_domain_event()
        return notification

    def record_created_domain_event(self) -> None:
        CREATED_DOMAIN_EVENTS = {
            "SLACK": NotificationSlackCreatedDomainEvent,
            "EMAIL": NotificationEmailCreatedDomainEvent,
        }
        event_class = CREATED_DOMAIN_EVENTS.get(self.topic.value.upper(), None)
        if not event_class:
            raise ValueError("The topic value is invalid")
        self.record_domain_event(
            event_class(id=self.id, topic=self.topic, description=self.description)
        )

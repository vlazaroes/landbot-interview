from pydantic import BaseModel

from contexts.notifications.domain.events.notification_created_domain_event import (
    NotificationCreatedDomainEvent,
)


class NotificationSlackCreatedDomainEvent(NotificationCreatedDomainEvent, BaseModel):
    def get_event_name(self) -> str:
        return "landbot.event.notification.slack.created"

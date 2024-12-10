from src.contexts.notifications.domain.events.notification_created_domain_event import (
    NotificationCreatedDomainEvent,
)


class NotificationEmailCreatedDomainEvent(NotificationCreatedDomainEvent):
    def get_event_name(self) -> str:
        return "landbot.event.notification.email.created"

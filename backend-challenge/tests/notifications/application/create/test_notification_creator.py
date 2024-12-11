import pytest

from src.contexts.notifications.application.create.notification_creator import (
    NotificationCreator,
)
from src.contexts.notifications.domain.events.notification_email_created_domain_event import (
    NotificationEmailCreatedDomainEvent,
)
from src.contexts.notifications.domain.events.notification_slack_created_domain_event import (
    NotificationSlackCreatedDomainEvent,
)
from src.contexts.shared.domain.events.event_bus import (
    EventBus,
)


@pytest.fixture
def event_bus(mocker) -> EventBus:
    return mocker.patch(
        "src.contexts.shared.domain.events.event_bus.EventBus"
    ).return_value


@pytest.fixture
def notification_creator(event_bus: EventBus) -> NotificationCreator:
    return NotificationCreator(event_bus=event_bus)


class TestNotificationCreator:
    def test_should_publish_domain_events(
        self, notification_creator: NotificationCreator, event_bus: EventBus
    ) -> None:
        notification_creator.run("Pricing", "Lorem ipsum dolor sit amet")
        event_bus.publish_domain_events.assert_called_once()

    def test_should_be_slack_domain_event(
        self, notification_creator: NotificationCreator, event_bus: EventBus
    ) -> None:
        notification_creator.run("Sales", "Lorem ipsum dolor sit amet")
        notification = event_bus.publish_domain_events.call_args[0][0][0]
        assert isinstance(notification, NotificationSlackCreatedDomainEvent)

    def test_should_be_email_domain_event(
        self, notification_creator: NotificationCreator, event_bus: EventBus
    ) -> None:
        notification_creator.run("Pricing", "Lorem ipsum dolor sit amet")
        notification = event_bus.publish_domain_events.call_args[0][0][0]
        assert isinstance(notification, NotificationEmailCreatedDomainEvent)

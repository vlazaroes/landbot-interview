import datetime
import json
import uuid

import pytest

from src.contexts.notifications.domain.events.notification_slack_created_domain_event import (
    NotificationSlackCreatedDomainEvent,
)
from src.contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from src.contexts.notifications.domain.notification_id import NotificationId
from src.contexts.notifications.domain.notification_topic import NotificationTopic


@pytest.fixture
def domain_event() -> NotificationSlackCreatedDomainEvent:
    return NotificationSlackCreatedDomainEvent(
        id=NotificationId(value=uuid.uuid4()),
        topic=NotificationTopic(value="Pricing"),
        description=NotificationDescription(value="Lorem ipsum dolor sit amet"),
    )


class TestNotificationCreatedDomainEvent:
    def test_should_have_valid_event_id(
        self, domain_event: NotificationSlackCreatedDomainEvent
    ) -> None:
        assert uuid.UUID(domain_event.get_event_id())

    def test_should_have_valid_creation_date(
        self, domain_event: NotificationSlackCreatedDomainEvent
    ) -> None:
        assert datetime.datetime.strptime(
            domain_event.get_ocurred_on(), "%Y-%m-%d %H:%M:%S.%f"
        )

    def test_should_have_event_name(
        self, domain_event: NotificationSlackCreatedDomainEvent
    ) -> None:
        assert (
            domain_event.get_event_name() == "landbot.event.notification.slack.created"
        )

    def test_should_serialize_its_fields(
        self, domain_event: NotificationSlackCreatedDomainEvent
    ) -> None:
        serialization = json.loads(domain_event.serialize())
        assert serialization["data"]["id"] == domain_event.get_event_id()
        assert serialization["data"]["type"] == domain_event.get_event_name()
        assert serialization["data"]["ocurred_on"] == domain_event.get_ocurred_on()
        assert serialization["data"]["attributes"]["id"] == str(domain_event.id.value)
        assert serialization["data"]["attributes"]["topic"] == str(
            domain_event.topic.value
        )
        assert serialization["data"]["attributes"]["description"] == str(
            domain_event.description.value
        )

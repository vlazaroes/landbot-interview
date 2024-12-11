import uuid

import pytest

from src.contexts.notifications.domain.events.notification_email_created_domain_event import (
    NotificationEmailCreatedDomainEvent,
)
from src.contexts.notifications.domain.notification import Notification
from src.contexts.notifications.domain.notification_description import (
    NotificationDescription,
)
from src.contexts.notifications.domain.notification_id import NotificationId
from src.contexts.notifications.domain.notification_topic import NotificationTopic


class TestNotification:
    def test_should_create_valid_notification(self) -> None:
        notification = Notification.create(
            id=NotificationId(value=uuid.uuid4()),
            topic=NotificationTopic(value="Pricing"),
            description=NotificationDescription(value="Lorem ipsum dolor sit amet"),
        )
        assert isinstance(notification, Notification)

    def test_should_raise_exception(self) -> None:
        with pytest.raises(ValueError):
            Notification.create(
                id=NotificationId(value=uuid.uuid4()),
                topic=NotificationTopic(value="Other"),
                description=NotificationDescription(value="Lorem ipsum dolor sit amet"),
            )

    def test_should_pull_domain_events(self) -> None:
        notification = Notification.create(
            id=NotificationId(value=uuid.uuid4()),
            topic=NotificationTopic(value="Pricing"),
            description=NotificationDescription(value="description"),
        )
        assert isinstance(
            notification.pull_domain_events()[0], NotificationEmailCreatedDomainEvent
        )

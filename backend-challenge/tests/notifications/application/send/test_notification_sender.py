import pytest

from src.contexts.notifications.application.send.notification_sender import (
    NotificationSender,
)
from src.contexts.notifications.domain.notifier import Notifier


@pytest.fixture
def notifier(mocker) -> Notifier:
    return mocker.patch(
        "src.contexts.notifications.domain.notifier.Notifier"
    ).return_value


@pytest.fixture
def notification_sender(notifier: Notifier) -> NotificationSender:
    return NotificationSender(notifier=notifier)


class TestNotificationSender:
    def test_should_send_notification(
        self, notification_sender: NotificationSender, notifier: Notifier
    ) -> None:
        notification_sender.run(
            "2fc8cdef-2395-414d-9da3-507f7f3fadf1",
            "Pricing",
            "Lorem ipsum dolor sit amet",
        )
        notifier.notify.assert_called_once()

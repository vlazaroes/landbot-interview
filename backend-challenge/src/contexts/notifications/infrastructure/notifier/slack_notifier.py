from slack_sdk import WebClient

from contexts.notifications.domain.notification import Notification
from contexts.notifications.domain.notifier import Notifier


class SlackNotifier(Notifier):
    def __init__(self, bot_token: str, channel_id: str) -> None:
        self.__client = WebClient(token=bot_token)
        self.__channel_id = channel_id

    def notify(self, notification: Notification) -> None:
        self.__client.chat_postMessage(
            channel=self.__channel_id,
            text=f"🔔 *Webhook Notification*: {notification.description.value}",
        )

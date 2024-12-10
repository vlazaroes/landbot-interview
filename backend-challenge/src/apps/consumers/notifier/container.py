import os

from dependency_injector import containers, providers

from contexts.notifications.application.send.notification_sender import (
    NotificationSender,
)
from contexts.notifications.infrastructure.notifier.email_notifier import EmailNotifier
from contexts.notifications.infrastructure.notifier.slack_notifier import SlackNotifier
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_connection import (
    RabbitMQConnection,
)
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_consumer import (
    RabbitMQConsumer,
)


def get_notifier_implementation(queue: str):
    match queue:
        case "webhooks.notifications.slack":
            return providers.Factory(
                SlackNotifier,
                bot_token=os.environ.get("SLACK_BOT_TOKEN"),
                channel_id=os.environ.get("SLACK_CHANNEL_ID"),
            )
        case "webhooks.notifications.email":
            return providers.Factory(
                EmailNotifier,
                hostname=os.environ.get("SMTP_HOSTNAME"),
                port=os.environ.get("SMTP_PORT"),
                username=os.environ.get("SMTP_USERNAME"),
                password=os.environ.get("SMTP_PASSWORD"),
                sender=os.environ.get("SMTP_SENDER"),
                recipient=os.environ.get("SMTP_RECIPIENT"),
            )
        case _:
            raise ValueError("The topic value is invalid")


class Container(containers.DeclarativeContainer):
    rabbitmq_connection = providers.Factory(
        RabbitMQConnection,
        hostname=os.environ.get("RABBITMQ_HOSTNAME"),
        username=os.environ.get("RABBITMQ_USERNAME"),
        password=os.environ.get("RABBITMQ_PASSWORD"),
    )
    rabbitmq_consumer = providers.Factory(
        RabbitMQConsumer,
        connection=rabbitmq_connection,
        exchange_name=os.environ.get("RABBITMQ_EXCHANGE"),
    )
    notifier = get_notifier_implementation(os.environ.get("RABBITMQ_QUEUE"))
    notification_sender = providers.Factory(
        NotificationSender,
        notifier=notifier,
    )

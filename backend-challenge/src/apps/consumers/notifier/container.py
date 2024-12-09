from dependency_injector import containers, providers

from contexts.notifications.application.send.notification_sender import (
    NotificationSender,
)
from contexts.notifications.infrastructure.notifier.slack_notifier import SlackNotifier
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_connection import (
    RabbitMQConnection,
)
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_consumer import (
    RabbitMQConsumer,
)


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    rabbitmq_connection = providers.Factory(
        RabbitMQConnection,
        hostname="localhost",
        username="landbot",
        password="landbot",
    )
    rabbitmq_consumer = providers.Factory(
        RabbitMQConsumer,
        connection=rabbitmq_connection,
        exchange_name="landbot.webhooks",
    )
    slack_notifier = providers.Factory(
        SlackNotifier,
    )
    notification_sender = providers.Factory(
        NotificationSender,
        notifier=slack_notifier,
    )

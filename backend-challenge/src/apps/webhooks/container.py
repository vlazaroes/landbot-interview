import os

from dependency_injector import containers, providers

from src.contexts.notifications.application.create.notification_creator import (
    NotificationCreator,
)
from src.contexts.shared.infrastructure.events.rabbitmq.rabbitmq_connection import (
    RabbitMQConnection,
)
from src.contexts.shared.infrastructure.events.rabbitmq.rabbitmq_event_bus import (
    RabbitMQEventBus,
)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routers.notifications"])

    rabbitmq_connection = providers.Factory(
        RabbitMQConnection,
        hostname=os.environ.get("RABBITMQ_HOSTNAME"),
        username=os.environ.get("RABBITMQ_USERNAME"),
        password=os.environ.get("RABBITMQ_PASSWORD"),
    )
    rabbitmq_event_bus = providers.Factory(
        RabbitMQEventBus,
        connection=rabbitmq_connection,
        exchange_name=os.environ.get("RABBITMQ_EXCHANGE"),
    )
    notification_creator = providers.Factory(
        NotificationCreator,
        event_bus=rabbitmq_event_bus,
    )

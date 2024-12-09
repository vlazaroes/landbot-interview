from dependency_injector import containers, providers

from contexts.notifications.application.create.notification_creator import (
    NotificationCreator,
)
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_connection import (
    RabbitMQConnection,
)
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_event_bus import (
    RabbitMQEventBus,
)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routers.notifications"])
    config = providers.Configuration()

    rabbitmq_connection = providers.Factory(
        RabbitMQConnection,
        hostname="localhost",
        username="landbot",
        password="landbot",
    )
    rabbitmq_event_bus = providers.Factory(
        RabbitMQEventBus,
        connection=rabbitmq_connection,
        exchange_name="landbot.webhooks",
    )
    notification_creator = providers.Factory(
        NotificationCreator,
        event_bus=rabbitmq_event_bus,
    )

import json
from typing import Any

from dependency_injector.wiring import Provide, inject
from pika import BasicProperties

from apps.consumers.notifier.container import Container
from contexts.notifications.application.send.notification_sender import (
    NotificationSender,
)
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_consumer import (
    RabbitMQConsumer,
)


@inject
def main(
    rabbitmq_consumer: RabbitMQConsumer = Provide[Container.rabbitmq_consumer],
    notification_sender: NotificationSender = Provide[Container.notification_sender],
):
    def consumer(
        channel: Any, method: Any, properties: BasicProperties, body: bytes
    ) -> None:
        event = json.loads(body)
        notification_sender.run(
            event["data"]["attributes"]["id"],
            event["data"]["attributes"]["topic"],
            event["data"]["attributes"]["description"],
        )

    rabbitmq_consumer.consume_domain_events(
        "webhooks.notifications",
        "landbot.event.notification.slack.created",
        callback=consumer,
    )


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    main()

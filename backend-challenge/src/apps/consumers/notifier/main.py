import json
import logging
import os
import sys
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
) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Started consumer process.")

    def consumer(
        channel: Any, method: Any, properties: BasicProperties, body: bytes
    ) -> None:
        try:
            event = json.loads(body)
            notification_sender.run(
                id=event["data"]["attributes"]["id"],
                topic=event["data"]["attributes"]["topic"],
                description=event["data"]["attributes"]["description"],
            )
            logging.info(
                f"{os.environ.get("RABBITMQ_BINDING_KEY")} - \"{event["data"]["attributes"]["id"]}\""
            )
        except Exception:
            logging.error(
                f"{os.environ.get("RABBITMQ_BINDING_KEY")} - \"{event["data"]["attributes"]["id"]}\""
            )

    logging.info("Waiting for messages.")
    rabbitmq_consumer.consume_domain_events(
        queue_name=os.environ.get("RABBITMQ_QUEUE"),
        binding_key=os.environ.get("RABBITMQ_BINDING_KEY"),
        callback=consumer,
    )


if __name__ == "__main__":
    try:
        container = Container()
        container.wire(modules=[__name__])
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

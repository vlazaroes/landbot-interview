from pika import BasicProperties

from contexts.shared.domain.events.domain_event import DomainEvent
from contexts.shared.domain.events.event_bus import EventBus
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_connection import (
    RabbitMQConnection,
)


class RabbitMQEventBus(EventBus):
    def __init__(self, connection: RabbitMQConnection, exchange_name: str) -> None:
        self.connection = connection
        self.__exchange_name = exchange_name
        self.connection.use_exchange(name=self.__exchange_name)

    def publish_domain_events(self, domain_events: list[DomainEvent]) -> None:
        for domain_event in domain_events:
            self.connection.channel.basic_publish(
                exchange=self.__exchange_name,
                routing_key=domain_event.get_event_name(),
                body=domain_event.serialize(),
                properties=BasicProperties(
                    content_type="application/json",
                    content_encoding="UTF-8",
                    message_id=domain_event.get_event_id(),
                ),
            )

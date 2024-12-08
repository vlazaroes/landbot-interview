from pika import BasicProperties

from contexts.shared.domain.events.domain_event import DomainEvent
from contexts.shared.domain.events.event_bus import EventBus
from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_connection import (
    RabbitMQConnection,
)


class RabbitMQEventBus(EventBus):
    def __init__(self, connection: RabbitMQConnection, exchange_name: str) -> None:
        self.connection = connection
        self.exchange_name = exchange_name
        self.connection.use_exchange(name=self.exchange_name)

    def publish_domain_events(self, domain_events: list[DomainEvent]) -> None:
        for domain_event in domain_events:
            self.connection.channel.basic_publish(
                exchange=self.exchange_name,
                routing_key=domain_event.event_name(),
                body=domain_event.to_json(),
                properties=BasicProperties(message_id=domain_event.event_id()),
            )

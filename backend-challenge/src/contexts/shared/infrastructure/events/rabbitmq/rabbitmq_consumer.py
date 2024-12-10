from typing import Any, Callable

from pika import BasicProperties

from contexts.shared.infrastructure.events.rabbitmq.rabbitmq_connection import (
    RabbitMQConnection,
)


class RabbitMQConsumer:
    def __init__(self, connection: RabbitMQConnection, exchange_name: str) -> None:
        self.connection = connection
        self.__exchange_name = exchange_name
        self.connection.use_exchange(name=self.__exchange_name)

    def consume_domain_events(
        self,
        queue_name: str,
        binding_key: str,
        callback: Callable[[Any, Any, BasicProperties, bytes], None],
    ) -> None:
        self.connection.use_queue(
            name=queue_name, exchange_name=self.__exchange_name, binding_key=binding_key
        )
        self.connection.channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True
        )
        self.connection.channel.start_consuming()

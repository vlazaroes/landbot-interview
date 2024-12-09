from pika import BlockingConnection, ConnectionParameters, PlainCredentials


class RabbitMQConnection:
    __connection: BlockingConnection = None

    def __init__(self, hostname: str, username: str, password: str) -> None:
        self.__connection = self.__create_connection(
            hostname=hostname, username=username, password=password
        )
        self.channel = self.__connection.channel()

    def use_exchange(self, name: str) -> None:
        self.channel.exchange_declare(
            exchange=name, exchange_type="topic", durable=True
        )

    def use_queue(self, name: str, exchange_name: str, binding_key: str) -> None:
        self.channel.queue_declare(queue=name, durable=True)
        self.channel.queue_bind(
            queue=name, exchange=exchange_name, routing_key=binding_key
        )

    def __create_connection(
        self, hostname: str, username: str, password: str
    ) -> BlockingConnection:
        if not self.__connection:
            credentials = PlainCredentials(username=username, password=password)
            parameters = ConnectionParameters(host=hostname, credentials=credentials)
            return BlockingConnection(parameters=parameters)
        return self.__connection

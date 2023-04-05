from typing import Type, Any
from types import TracebackType
from aio_pika import connect, Message, IncomingMessage
import json

from app_Worcker.Worcker_handler import Worker_handler
from app_rabbitMQ.settings import settings


print(settings.rabbit_dsn)








class RabbitClient(Worker_handler):

    def __init__(self):
        super().__init__()
        self.connect_rabbit: connect = connect(url=settings.rabbit_dsn,)


    async def put(self, connection: connect, message_data: Any, queue_name: str):
        # Creating a channel
        channel = await connection.channel()
        # Declaring queue
        callback_queue=await channel.declare_queue(queue_name)
        # Sending the message
        await channel.default_exchange.publish(
            Message(str(message_data).encode(), reply_to=callback_queue.name),
            routing_key=queue_name,
        )

    # @classmethod
    # async def on_message(cls, message: IncomingMessage):
    #     async with message.process():
    #         result = message.body.decode()
    #         # await cls.handler(result)



    async def receive(self, connection: connect, queue_name: str):
        # channel = await connection.channel()
        # await channel.set_qos(prefetch_count=1)
        # queue = await channel.declare_queue(queue_name)
        # await queue.consume(cls.on_message, no_ack=False)
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=5)
        queue = await channel.declare_queue(queue_name)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    result = message.body.decode()
                    print(eval(result))
                    await self.handler(eval(result))



    async def __aenter__(self) -> connect:
        return await self.connect_rabbit

    async def __aexit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None,
                        tb: TracebackType | None):
        self.connect_rabbit.close()

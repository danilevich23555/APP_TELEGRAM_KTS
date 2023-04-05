import asyncio
from aio_pika import IncomingMessage

from app_rabbitMQ.rabbit_client import RabbitClient



class Worker():

    def __init__(self, queue_name):
        self.is_running = False
        self.queue_name = queue_name
        self._task: list[asyncio.Task] = []

    async def _worker(self):
        while self.is_runing:
            async with RabbitClient() as connection:
                await RabbitClient.receive(connection, self.queue_name)

    async def handler(self, message: IncomingMessage):




    def start(self):
        self.is_runing = True
        self._task = [asyncio.create_task(self._worker())]

start_worcker = Worker(queue_name='hello')
async def start():
    start_worcker.start()



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()

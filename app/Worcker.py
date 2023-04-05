import asyncio
from aio_pika import IncomingMessage

from app_rabbitMQ.rabbit_client import RabbitClient
from AIOHTTP_CLIENT_WORK.project.tg import TgClientWithFile
from AIOHTTP_CLIENT_WORK.project.dcs import Message
from AIOHTTP_CLIENT_WORK.project.s3 import S3Client
from AIOHTTP_CLIENT_WORK.project.sqllite_db import sqllite_DB
from AIOHTTP_CLIENT_WORK.project.redis import redis
from app_rabbitMQ.settings import settings

class Worker_handler():

    def __init__(self, token):
        self.s3 = S3Client(
            endpoint_url=settings.DSN_MINIO,
            aws_access_key_id=settings.MINIO_ACCESS_KEY,
            aws_secret_access_key=settings.MINIO_SECRET_KEY
        )
        self.tg_client = TgClientWithFile(token=token)
    async def handler(self, message):
        r = Message.Schema().load(message['message'])
        async with TgClientWithFile(settings.TELEGRAM_TOKEN) as tg_cli:
            if r.video == None:
                try:
                    for k in r.photo:
                        res_path = await tg_cli.get_file(k['file_id'])
                        await self.s3.fetch_and_upload('tests', f'{res_path.file_path[7:]}',
                                                     f'{tg_cli.API_FILE_PATH}{tg_cli.token}/{res_path.file_path}')
                except TypeError:
                    res_path = await tg_cli.get_file(r.document['file_id'])
                    await self.s3.fetch_and_upload('tests', f'{r.document["file_name"]}',
                                                 f'{tg_cli.API_FILE_PATH}{tg_cli.token}/{res_path.file_path}')



class Worker():

    def __init__(self, queue_name):
        self.is_running = False
        self.queue_name = queue_name
        self._task: list[asyncio.Task] = []

    async def _worker(self):
        while self.is_runing:
            async with RabbitClient() as connection:
                await RabbitClient.receive(connection, self.queue_name)



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

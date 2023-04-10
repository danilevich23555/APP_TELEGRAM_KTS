import asyncio
import os

from telegramm.tg import TgClientWithFile
from telegramm.dcs import Message
from sqlite.sqllite_db import sqllite_DB
from app_rabbitMQ.rabbit_client import RabbitClient
from settings.settings import settings


class Poller:

    def __init__(self, token):
        self.tg_client = TgClientWithFile(token)
        self.is_running = False
        self.sql = sqllite_DB(os.path.join(os.getcwd(), 'update_chat_id.db'))
        self._task = asyncio.Task


    async def _worker(self):
        while self.is_running:
            res = await self.tg_client.get_updates()
            for x in res['result']:
                r = Message.Schema().load(x['message'])
                response_id = await self.sql.select_id(r.chat.id)
                if response_id == None:
                    response_id = (0, 0)
                if x['update_id'] > int(response_id[0]):
                    await self.sql.insert_records((x['update_id'], r.chat.id))
                    async with RabbitClient() as rabbit:
                        await rabbit.put(message_data=f"{x['message']}", queue_name='hello_1')

    async def start(self):
        self.is_running = True
        self._task = await asyncio.create_task(self._worker())




if __name__ == '__main__':
    poller = Poller(settings.TELEGRAM_TOKEN)
    loop = asyncio.get_event_loop()
    loop.create_task(poller.start())
    loop.run_forever()






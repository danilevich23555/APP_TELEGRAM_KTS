import asyncio
import datetime

from app_rabbitMQ.rabbit_client import RabbitClient




async def start_sender():
    async with RabbitClient() as connection:
        await RabbitClient.put(connection=connection,message_data='sadfsdafdas'+f'{datetime.datetime.now()}',
                                   queue_name='hello')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_sender())
    loop.run_forever()
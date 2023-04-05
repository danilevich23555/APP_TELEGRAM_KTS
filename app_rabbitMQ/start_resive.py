import asyncio

from app_rabbitMQ.rabbit_client import RabbitClient




async def start_resive():
    async with RabbitClient() as connection:
        await RabbitClient.receive(connection=connection,
                                   queue_name='hello')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_resive())
    loop.run_forever()
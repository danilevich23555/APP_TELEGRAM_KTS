import asyncio
import datetime

from app_rabbitMQ.rabbit_client import RabbitClient


# async def start_sender():
#     async with RabbitClient() as rabbit:
#         await rabbit.put(message_data="{'message_id': 352, 'from': {'id': 759589704, 'is_bot': False, 'first_name': 'Danila', 'username': 'daniladolgov', 'language_code': 'ru'}, 'chat': {'id': 759589704, 'first_name': 'Danila', 'username': 'daniladolgov', 'type': 'private'}, 'date': 1680720030, 'document': {'file_name': 'Книга_Девид Базали', 'mime_type': 'application/octet-stream', 'file_id': 'BQACAgIAAxkBAAIBYGQtwJ426I8mVXlcy0RJwHobiOtdAAIlIwACYt-QSwZJsO0i38OOLwQ', 'file_unique_id': 'AgADJSMAAmLfkEs', 'file_size': 12403084}}",
#                                    queue_name='hello_1')

async def start_sender():
    async with RabbitClient() as rabbit:
        await rabbit.put(message_data="{'message_id': 351, 'from': {'id': 759589704, 'is_bot': False, 'first_name': 'Danila', 'username': 'daniladolgov', 'language_code': 'ru'}, 'chat': {'id': 759589704, 'first_name': 'Danila', 'username': 'daniladolgov', 'type': 'private'}, 'date': 1680689028, 'photo': [{'file_id': 'AgACAgIAAxkBAAIBX2QtR4Q7K1ajwVKRkVxIV_EJuzpRAAIawjEbhS9oSSquAAEwzHmA0gEAAwIAA3MAAy8E', 'file_unique_id': 'AQADGsIxG4UvaEl4', 'file_size': 1168, 'width': 67, 'height': 90}, {'file_id': 'AgACAgIAAxkBAAIBX2QtR4Q7K1ajwVKRkVxIV_EJuzpRAAIawjEbhS9oSSquAAEwzHmA0gEAAwIAA20AAy8E', 'file_unique_id': 'AQADGsIxG4UvaEly', 'file_size': 14729, 'width': 240, 'height': 320}, {'file_id': 'AgACAgIAAxkBAAIBX2QtR4Q7K1ajwVKRkVxIV_EJuzpRAAIawjEbhS9oSSquAAEwzHmA0gEAAwIAA3gAAy8E', 'file_unique_id': 'AQADGsIxG4UvaEl9', 'file_size': 65458, 'width': 600, 'height': 800}, {'file_id': 'AgACAgIAAxkBAAIBX2QtR4Q7K1ajwVKRkVxIV_EJuzpRAAIawjEbhS9oSSquAAEwzHmA0gEAAwIAA3kAAy8E', 'file_unique_id': 'AQADGsIxG4UvaEl-', 'file_size': 84520, 'width': 960, 'height': 1280}]}",
                                   queue_name='hello_1')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_sender())
    loop.run_forever()
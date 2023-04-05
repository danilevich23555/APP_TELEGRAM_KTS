import aioredis
import asyncio
import json


from redis import redis

test = {'update_id': 292714652, 'message': {'message_id': 147, 'from': {'id': 1096938346, 'is_bot': False, 'first_name': 'Nikita', 'last_name': 'Dolgov', 'username': 'Kitos2308', 'language_code': 'ru'}, 'chat': {'id': 1096938346, 'first_name': 'Nikita', 'last_name': 'Dolgov', 'username': 'Kitos2308', 'type': 'private'}, 'date': 1676370832, 'media_group_id': '13410966661894498', 'photo': [{'file_id': 'AgACAgIAAxkBAAOUY-tjkGvFkxR3Mw9ZZ_x0WWc-F_cAAnPEMRtlkVlLN9JKCD3SBdQBAAMCAANzAAMuBA', 'file_unique_id': 'AQADc8QxG2WRWUt4', 'file_size': 1567, 'width': 67, 'height': 90}, {'file_id': 'AgACAgIAAxkBAAOUY-tjkGvFkxR3Mw9ZZ_x0WWc-F_cAAnPEMRtlkVlLN9JKCD3SBdQBAAMCAANtAAMuBA', 'file_unique_id': 'AQADc8QxG2WRWUty', 'file_size': 21072, 'width': 240, 'height': 320}, {'file_id': 'AgACAgIAAxkBAAOUY-tjkGvFkxR3Mw9ZZ_x0WWc-F_cAAnPEMRtlkVlLN9JKCD3SBdQBAAMCAAN4AAMuBA', 'file_unique_id': 'AQADc8QxG2WRWUt9', 'file_size': 94438, 'width': 600, 'height': 800}, {'file_id': 'AgACAgIAAxkBAAOUY-tjkGvFkxR3Mw9ZZ_x0WWc-F_cAAnPEMRtlkVlLN9JKCD3SBdQBAAMCAAN5AAMuBA', 'file_unique_id': 'AQADc8QxG2WRWUt-', 'file_size': 131934, 'width': 960, 'height': 1280}]}}


# client = redis.Redis(host='127.0.0.1', port=6379, db=0)
#
#
# client.json().set('data', '$', test)
#
# result = client.json().get('data')
# print(result)



async def main():
    redis_test = redis('redis://localhost', 0)
    await redis_test.redis_put('1', test)
    value = await redis_test.redis_get('1')
    print(value)




if __name__ == "__main__":
    asyncio.run(main())


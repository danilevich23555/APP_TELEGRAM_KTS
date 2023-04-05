import asyncio
from decouple import config
import json

from tg import TgClientWithFile
from dcs import Message
from s3 import S3Client
from sqllite_db import sqllite_DB
from redis import redis








async def cli():
    scl = sqllite_DB('update_chat_id.db')
    redis_int = redis('redis://localhost', 0)
    async with TgClientWithFile(config('TELEGRAM_TOKEN')) as tg_cli:
        res = await tg_cli.get_updates()
        for x in res['result']:
            r = Message.Schema().load(x['message'])
            response_id = await scl.select_id(r.chat.id)
            if response_id == None:
                response_id = (0, 0)
            if x['update_id'] > int(response_id[0]):
                    await redis_int.redis_put(f'{x["update_id"]}', x)
                    await scl.insert_records((x['update_id'], r.chat.id))



async def run_uploader():
    redis_int = redis('redis://localhost', 0)
    keys = await redis_int.keys_get()
    cr = dict(
        endpoint_url=config('DSN_MINIO'),
        aws_secret_access_key=config('MINIO_ACCESS_KEY'),
        aws_access_key_id=config('MINIO_SECRET_KEY')
    )
    s3cli = S3Client(**cr)
    for key in keys:
        result = await redis_int.redis_get(key)
        r = Message.Schema().load(result['message'])
        async with TgClientWithFile(config('TELEGRAM_TOKEN')) as tg_cli:
            if r.video == None:
                try:
                    for k in r.photo:
                        res_path = await tg_cli.get_file(k['file_id'])
                        await s3cli.fetch_and_upload('tests', f'{res_path.file_path[7:]}',
                                                     f'{tg_cli.API_FILE_PATH}{tg_cli.token}/{res_path.file_path}')
                except TypeError:
                    res_path = await tg_cli.get_file(r.document['file_id'])
                    await s3cli.fetch_and_upload('tests', f'{r.document["file_name"]}',
                                                 f'{tg_cli.API_FILE_PATH}{tg_cli.token}/{res_path.file_path}')
                await redis_int.del_key(key)




async def worker():
    cr = dict(
        endpoint_url=config('DSN_MINIO'),
        aws_secret_access_key=config('MINIO_ACCESS_KEY'),
        aws_access_key_id=config('MINIO_SECRET_KEY')
    )
    s3cli = S3Client(**cr)
    response_bucket = await s3cli.list_buckets()
    print(x for x in response_bucket['Buckets'])
    if response_bucket['Buckets'] != []:
        for bucket in response_bucket['Buckets']:
            if bucket['Name'] == 'tests':
                break
            else:
                await s3cli.cr_bucket("tests")
    else:
        scl = sqllite_DB('update_chat_id.db')
        await scl.create_table()
        await s3cli.cr_bucket("tests")
    while True:
        await cli()
        await run_uploader()




if __name__ == '__main__':
    asyncio.run(worker())


from telegramm.tg import TgClientWithFile
from telegramm.dcs import Message
from s3_MINIO.s3 import S3Client
from settings.settings import settings


class Worker_handler:

    def __init__(self):
        self.token = settings.TELEGRAM_TOKEN
        self.s3 = S3Client(
            endpoint_url=settings.DSN_MINIO,
            aws_access_key_id=settings.MINIO_ACCESS_KEY,
            aws_secret_access_key=settings.MINIO_SECRET_KEY
        )
        self.tg_client = TgClientWithFile(token=self.token)

    async def handler(self, message):
        r = Message.Schema().load(message)
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
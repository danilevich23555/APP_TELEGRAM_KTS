import aioredis
import json


class redis():
    def __init__(self, DSN_REDIS, DB):
        self.redis = aioredis.from_url(DSN_REDIS, db=DB)

    async def redis_put(self, chat_id, data_tg_update):
        await self.redis.set(f"{chat_id}", json.dumps(data_tg_update))

    async def redis_get(self, update_id):
        value = await self.redis.get(update_id)
        return json.loads(value)

    async def keys_get(self):
        keys = await self.redis.keys()
        return keys

    async def del_key(self, key):
        await self.redis.delete(key)


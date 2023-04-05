import asyncio
import aiosqlite

from sqllite_db import sqllite_DB


temp= [(3,3), (4,4)]

scl = sqllite_DB('update_chat_id.db')
async def test():
    # await scl.create_table()
    # await scl.insert_records((2927, 759))
    await scl.select_id()


asyncio.run(test())


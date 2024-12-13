import aiosqlite
import asyncio

async def async_fetch_users(database):
    async with aiosqlite.connect(database=database) as asynccursor:
        query = "SELECT * FROM users"
        async with asynccursor.execute(query) as cursor:
            allData = await cursor.fetchall()
            for row in allData:
                print(row)


async def async_fetch_older_users(database):
    async with aiosqlite.connect(database=database) as asynccursor:
        query = "SELECT * FROM users where age > 40"
        async with asynccursor.execute(query) as cursor:
            allData = await cursor.fetchall()
            for row in allData:
                print(row)

async def fetch_concurrently():
    result = await asyncio.gather(async_fetch_users('users.db'
    ), async_fetch_older_users('users.db'))
    return result

asyncio.run(fetch_concurrently())

import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as asynccursor:
        query = "SELECT * FROM users"
        async with asynccursor.execute(query) as cursor:
            allData = await cursor.fetchall()
            for row in allData:
                print(row)


async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as asynccursor:
        query = "SELECT * FROM users where age > 40"
        async with asynccursor.execute(query) as cursor:
            allData = await cursor.fetchall()
            for row in allData:
                print(row)

async def fetch_concurrently():
    result = await asyncio.gather(async_fetch_users(), 
    async_fetch_older_users())
    return result

asyncio.run(fetch_concurrently())

"""
Checks if Prisma is connected to database
"""

import asyncio

from prisma import Prisma


async def check_connection():
    db = Prisma()
    await db.connect()
    print("Connected to the database!")
    await db.disconnect()


asyncio.run(check_connection())

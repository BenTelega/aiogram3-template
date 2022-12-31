import asyncio

import bot
from services import APScheduler 

async def main():
    # APScheduler.setup()
    await bot.setup()

if __name__ == "__main__":
    asyncio.run(main())
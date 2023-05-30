import asyncio, logging
from aiogram import Dispatcher, Bot
from env import BOT_TOKEN
from services import APScheduler 

from handlers import user

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    APScheduler.setup()

    dp = Dispatcher()
    dp.include_router(user.router)
    bot = Bot(BOT_TOKEN, parse_mode='html')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
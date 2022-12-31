from modules import * 
from handlers import user, admin

async def setup():
    dp = Dispatcher()
    dp.include_router(user.router)
    dp.include_router(admin.router)

    # setting up middlewares 
    # tech_works.setup(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
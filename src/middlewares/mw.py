from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram import types, Dispatcher
from typing import * 

async def get_testers() -> List[int]:
    return []


class BotMiddlewere(BaseMiddleware):
    async def __call__(self, 
        handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: types.Update,
        data: Dict[str, Any]
    ):
        return await handler(event, data)

def setup(dp: Dispatcher):
    dp.message.middleware(BotMiddlewere())
    dp.callback_query.middleware(BotMiddlewere())
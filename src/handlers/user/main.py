from aiogram import Router, filters, F, types
from utils import functions
from keyboards import *

router = Router()

@router.message(filters.Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('<b>Hello!</b>', reply_markup=MENU)

    result = functions.check_start_command(message.text)
    if result['exist']:
        await functions.handler_start_command(message, result['data']['command'], result['data']['data'])

from aiogram import Router, filters, F, types
from utils import functions
from keyboards import *

router = Router()


class AdminFilter(filters.BaseFilter): 
    async def __call__(self, message: types.Message) -> bool:
        pass

router.message.filter(AdminFilter())

@router.message(filters.Command("admin"))
async def cmd_admin(message: types.Message):
    await message.answer('<b>Админ-Панель</b>', reply_markup=ADMIN)

@router.message(filters.Text('⬅️ Назад'))
async def cmd_back(message: types.Message):
    await message.answer('<b>Меню</b>', reply_markup=MENU)
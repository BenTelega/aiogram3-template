from modules import * 
from aiogram.filters import BaseFilter
from utils import functions

router = Router()


class AdminFilter(BaseFilter): 
    async def __call__(self, message: types.Message) -> bool:
        pass

router.message.filter(AdminFilter())

@router.message(filters.Text('⬅️ Назад'))
async def cmd_back(message: types.Message):
    await message.answer('<b>Меню</b>', reply_markup=MENU)
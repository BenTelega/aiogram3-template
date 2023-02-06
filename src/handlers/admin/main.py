from modules import * 
from utils import functions

router = Router()

@router.message(filters.Text('⬅️ Назад'))
async def cmd_back(message: types.Message):
    await message.answer('<b>Меню</b>', reply_markup=MENU)
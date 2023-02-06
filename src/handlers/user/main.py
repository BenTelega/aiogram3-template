from modules import * 
from utils import functions

router = Router()

@router.message(filters.Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('<b>Hello!</b>', reply_markup=MENU)

    result = functions.check_start_command(message.text)
    if result['exist']:
        await functions.handler_start_command(message, result['data']['command'], result['data']['data'])

@router.message(filters.Command("admin"), F.from_user.id.in_(db.json_config.get_value('admins')))
async def cmd_admin(message: types.Message):
    await message.answer('<b>Админ-Панель</b>', reply_markup=ADMIN)

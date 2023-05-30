from aiogram import Router, filters, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import *

class Form(StatesGroup):
    name = State()
    age = State()

router = Router()

router.message.filter(filters.StateFilter(Form))

@router.message(filters.Text('⬅️ Назад'))
async def back(message: types.Message, state: FSMContext):
    await message.answer(f'<b>Меню</b>', reply_markup=MENU)
    await state.clear()

@router.message(Form.name)
async def form(message: types.Message, state: FSMContext):
    await message.answer('Теперь введи возраст:')
    await state.update_data(name=message.text)
    await state.set_state(Form.age)

@router.message(Form.age)
async def form(message: types.Message, state: FSMContext):
    await message.answer(f'Твои данные\n\n{(await state.get_data())["name"]} Возраст: {message.text}')
    await state.clear()
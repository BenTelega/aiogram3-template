from typing import List 
from modules import types

def k_formatter(array: List[list]) -> types.ReplyKeyboardMarkup:
    keyboard = [[]]
    line_index = 0
    for row in array:
        for button in row:
            keyboard[line_index].append(types.KeyboardButton(text=button))

        keyboard.append([])
        line_index += 1

    return types.ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )

def menu() -> types.ReplyKeyboardMarkup:
    return k_formatter([
        ["Button"]
    ]) 

def admin() -> types.ReplyKeyboardMarkup:
    return k_formatter([
        ["⬅️ Назад"]
    ]) 

def back() -> types.ReplyKeyboardMarkup:
    return k_formatter([
        ["⬅️ Назад"]
    ])
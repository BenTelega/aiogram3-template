import aiogram, logging
from typing import *

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, filters

from aiogram.fsm.context import FSMContext
# #from aiogram.contrib.fsm_storage.mongo import MongoStorage

from settings import config
from utils.middlewares import tech_works

from utils import keyboards

# logger setting up
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# bot setting up
bot = Bot(token=config.BOT_TOKEN, parse_mode='html')

# keyboards setting up
MENU = keyboards.menu()
ADMIN = keyboards.admin()
BACK = keyboards.back()
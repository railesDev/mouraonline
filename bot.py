# Bot setup

from config_reader import config
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from main import c, conn
import asyncio
from aiogram.enums import ParseMode
import handlers

storage = MemoryStorage()
moura = Bot(token=config.bot_token.get_secret_value(), parse_mode='HTML')
dp = Dispatcher(storage=storage)
router = Router()
dp.include_router(router)

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.admin import admin_main_menu_def
from loader import dp
from main.config import ADMINS


@dp.message_handler(CommandStart(), chat_id=ADMINS)
async def bot_start(message: types.Message):
    text = "👋 Salom admin botga xush kelibsiz !"
    await message.answer(text=text, reply_markup=await admin_main_menu_def())

import re
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin import admin_main_menu_def
from keyboards.default.back import main_menu_back
from loader import dp
from main.config import ADMINS
from states.AddPubgAccount import AddPubgAccountState
from utils.db_commands.accounts import add_account


@dp.message_handler(text="👤➕ Pubg akkound qo'shish", state="*", chat_id=ADMINS)
async def add_film_handler(message: types.Message):
    text = "📧 Iltimos, accountni emailini kiriting"
    await message.answer(text=text, reply_markup=await main_menu_back())
    await AddPubgAccountState.email.set()


@dp.message_handler(state=AddPubgAccountState.email, chat_id=ADMINS)
async def add_film_handler(message: types.Message, state: FSMContext):
    email = message.text
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(email_regex, email):
        await state.update_data(email=email, created_at=message.date)
        text = "🔑 Iltimos, accountni parolini kiriting."
        await message.answer(text=text)
        await AddPubgAccountState.password.set()
    else:
        error_text = "❌ Iltimos, to'g'ri email manzilini kiriting."
        await message.answer(text=error_text)


@dp.message_handler(state=AddPubgAccountState.password, chat_id=ADMINS)
async def add_film_handler(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    if await add_account(data=data):
        text = "✅ Account qo'shildi."
        await message.answer(text=text)
        await state.finish()
    else:
        text = "❌ Account qo'shishda xatolik bor."
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()

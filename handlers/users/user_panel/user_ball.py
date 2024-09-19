from aiogram import types

from keyboards.default.user import user_main_menu_def
from loader import dp
from main.config import CHANNEL_ID
from utils.db_commands.users import get_user_data, get_user, add_user


@dp.message_handler(text="🏅 Mening ballim")
async def referral_link_handler(message: types.Message):
    if await get_user(chat_id=message.chat.id):
        user_data = await get_user_data(chat_id=message.chat.id)
        text = f"🎯 Sizning {user_data['suggested']}ta ballingiz bor"
        await message.answer(text=text, reply_markup=await user_main_menu_def())
    else:
        if await add_user(message=message):
            user_data = await get_user_data(chat_id=message.chat.id)
            text = f"🎯 Sizning {user_data['suggested']}ta ballingiz bor"
            await message.answer(text=text, reply_markup=await user_main_menu_def())
        else:
            error_text = "⚠️ Bizda user qo'shish qismida muamo chiqdi biz bilan bog'laning."
            await message.answer(text=error_text)

from aiogram import types

from keyboards.default.user import user_main_menu_def
from loader import dp
from main.config import CHANNEL_ID
from utils.db_commands.users import get_user_data


@dp.message_handler(text="🏅 Mening ballim")
async def referral_link_handler(message: types.Message):
    user_data = await get_user_data(chat_id=message.chat.id)
    text = f"🎯 Sizning {user_data['suggested']}ta ballingiz bor"
    await message.answer(text=text, reply_markup=await user_main_menu_def())

from aiogram import types

from keyboards.default.user import user_main_menu_def
from loader import dp
from main.config import CHANNEL_ID
from utils.db_commands.users import get_user_data


@dp.message_handler(text="🏅 Mening ballim")
async def referral_link_handler(message: types.Message):
    if int(message.chat.id) == CHANNEL_ID:
        pass
    else:
        user_data = await get_user_data(chat_id=message.chat.id)
        text = (
            f"🎯 Sizning ballaringiz:\n"
            f"💯 Botda: {user_data['bot_suggested']} ball\n"
            f"💬 Gruppada: {user_data['chat_suggested']} ball"
        )
        await message.answer(text=text, reply_markup=await user_main_menu_def())

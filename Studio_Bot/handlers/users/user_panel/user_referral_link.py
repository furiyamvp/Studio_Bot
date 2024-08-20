from aiogram import types

from keyboards.default.user import user_main_menu_def
from loader import dp
from main.config import SHARE_LINK, CHANNEL_ID


@dp.message_handler(text="🎯 Ball yig'ish")
async def referral_link_handler(message: types.Message):
    if int(message.chat.id) == CHANNEL_ID:
        pass
    else:
        user_id = message.chat.id
        text = (
            f"🔗 Referral havola 👇\n\n{SHARE_LINK}{user_id}\n\n🎯 Har bir referral uchun 1 ball\n💯 29 ta odam qo'shsangiz tekin account yutib olasiz\n"
            f"\n👥 Guruhga ham odam qo'shangiz, bizni studio guruhimizga 29 ta odam qo'shsangiz tekin account yutib olasiz"
        )
        await message.answer(text=text, reply_markup=await user_main_menu_def())

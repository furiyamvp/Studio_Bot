from aiogram import types

from keyboards.default.user import user_main_menu_def
from loader import dp
from main.config import SHARE_LINK
from utils.db_commands.users import get_user, add_user


@dp.message_handler(text="🎯 Ball yig'ish")
async def referral_link_handler(message: types.Message):
    if await get_user(chat_id=message.chat.id):
        user_id = message.chat.id
        text = (
            f"🔗 Referral havola 👇\n\n{SHARE_LINK}{user_id}\n\n🎯 Har bir referral uchun +1 ball\n💯 29 ta odam qo'shsangiz tekin account yutib olasiz\n"
        )
        await message.answer(text=text, reply_markup=await user_main_menu_def())
    else:
        if await add_user(message=message):
            user_id = message.chat.id
            text = (
                f"🔗 Referral havola 👇\n\n{SHARE_LINK}{user_id}\n\n🎯 Har bir referral uchun +1 ball\n💯 29 ta odam qo'shsangiz tekin account yutib olasiz\n"
            )
            await message.answer(text=text, reply_markup=await user_main_menu_def())
        else:
            error_text = "Bizda user qo'shish qismida muamo chiqdi biz bilan bog'laning."
            await message.answer(text=error_text)

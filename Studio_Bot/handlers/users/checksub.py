from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from main.config import CHANNELS
from utils.db_commands.users import get_user
from utils.misc.subscription import check


@dp.callback_query_handler(text="check_subs", state="*")
async def check_subs_handler(call: types.CallbackQuery):
    result = "Siz kanalarga obuna bo'lmadingiz ❌"
    final_status = True
    markup = InlineKeyboardMarkup(row_width=1)

    for idx, channel in enumerate(CHANNELS, start=1):
        status = await check(user_id=int(call.message.chat.id), channel=channel[1])
        if not status:
            final_status = False
            button = InlineKeyboardButton(text=f"{idx} - kanal", url=channel[0])
            markup.add(button)

    if not final_status:
        markup.add(InlineKeyboardButton(text="⭕️ Obunani tekshirish", callback_data="check_subs"))
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=markup)
    else:
        if await get_user(call.message.chat.id):
            text = "Siz muvaffaqiyatli obuna boldingiz,\nBot ishga tushdi 🤖✅"
            await call.message.answer(text=text)
        else:
            text = "Siz muvaffaqiyatli obuna boldingiz,\nBot ishga tushdi 🤖✅"
            await call.message.answer(text=text)

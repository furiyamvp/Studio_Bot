from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from main.config import CHANNELS
from utils.misc import subscription


async def check_subs(message):
    result = "Botdan foydalanish uchun quyidagi kanalga obuna bo'ling:"
    final_status = True
    markup = InlineKeyboardMarkup(row_width=1)

    for channel in CHANNELS:
        status = await subscription.check(user_id=message.chat.id, channel=channel[1])
        if not status:
            final_status = False
            button = InlineKeyboardButton(text=channel[-1], url=channel[0])
            markup.add(button)

    if not final_status:
        markup.add(InlineKeyboardButton(text="Obunani tekshirish ⭕️", callback_data="check_subs"))
        await message.answer(result, reply_markup=markup)
        return True
    return False

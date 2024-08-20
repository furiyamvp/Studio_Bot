from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


subs_check = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Obunani tekshirish ✅", callback_data="check_subs")
    ]]
)

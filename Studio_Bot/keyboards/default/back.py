from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def main_menu_back():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("⬅️ Orqaga")
            ]
        ], resize_keyboard=True
    )
    return markup

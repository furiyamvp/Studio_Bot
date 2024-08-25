from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def admin_main_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("📊 Statistikalar")
            ],
            [
                KeyboardButton("👤➕ Pubg akkound qo'shish"),
            ],
        ], resize_keyboard=True
    )
    return markup


async def statistics_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("👥 Foydalanuvchilar soni"),
                KeyboardButton("👤 Obunachilar o'lgan akkountlar soni")
            ],
            [
                KeyboardButton("⬅️ Orqaga")
            ],
        ], resize_keyboard=True
    )
    return markup

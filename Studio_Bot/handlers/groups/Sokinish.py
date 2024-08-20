import re
from aiogram import types

from loader import dp


@dp.message_handler(regexp=r'\b(mashka|mawka|gandon|oneni ami|suka|buvini ami)\b')
async def on_text_message(message: types.Message):
    await message.delete()

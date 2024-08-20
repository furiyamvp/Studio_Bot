from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text="😊 Assalomu alaykum,\nSiz bu bot orqali studio pubg kanaliga kirib "
                              "10 ta odam qoshsangiz tekin akk yutib olasiz\n"
                              "👉 <a href='https://t.me/studio_pubgm_chat'>Pubg Studio CHAT</a>\n"
                         )

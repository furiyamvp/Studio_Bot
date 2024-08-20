from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from main.config import CHANNELS, ADMINS
from utils.misc.subscription import check


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs" or str(user) in ADMINS:
                return
        else:
            return

        final_status = True
        markup = InlineKeyboardMarkup(row_width=1)
        for idx, channel in enumerate(CHANNELS, start=1):
            status = await check(user_id=user, channel=channel[1])
            if not status:
                final_status = False
                button = InlineKeyboardButton(text=f"{idx} - kanal", url=channel[0])
                markup.add(button)

        if not final_status:
            markup.add(InlineKeyboardButton(text="Obunani tekshirish ⭕️\n", callback_data="check_subs"))
            await update.message.answer(
                "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling ❌",
                reply_markup=markup
            )
            raise CancelHandler()


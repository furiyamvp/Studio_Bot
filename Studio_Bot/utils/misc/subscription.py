from typing import Union
from aiogram import Bot
from aiogram.utils.exceptions import BadRequest


async def check(user_id: int, channel: Union[int, str]) -> bool:
    bot = Bot.get_current()
    try:
        member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        return member.is_chat_member() or member.status in ["creator", "administrator"]
    except BadRequest:
        # Handle cases where the user_id or chat_id is invalid
        return False

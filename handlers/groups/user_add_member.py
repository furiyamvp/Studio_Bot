from aiogram import types

from loader import dp
from utils.db_commands.users import update_user_suggested, add_user, get_user_with_id


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def on_new_chat_member(message: types.Message):
    new_user_id = message.new_chat_members[0]["id"]
    user_id = message.from_user.id
    date = message.date

    if await get_user_with_id(user_id):
        if await get_user_with_id(new_user_id):
            text = "Siz qo'shgan odam , bizni gruppamizda oldin bo'lgan, sizga ball berilmaydi."
            await message.answer(text=text)
        else:
            await add_user(chat_id=new_user_id, date=date)
            await update_user_suggested(chat_id=user_id, date=date)
            user = await get_user_with_id(user_id)
            number = 29
            if user.get("suggested") == number:
                text = ("Siz random tekin akk olishingiz mumkin\n"
                    "adminlar bilan bog'laning\n"
                    "1) @stud1o_pubgm")
                number += 29
                await message.reply(text=text)
    else:
        await add_user(user_id, date=date)
        if await get_user_with_id(new_user_id):
            text = "Siz qo'shgan odam , bizni gruppamizda oldin bo'lgan, sizga ball berilmaydi."
            await message.answer(text=text)
        else:
            await update_user_suggested(chat_id=user_id, date=date)
            await add_user(new_user_id, date=date)

from aiogram import types
from loader import dp, bot
from utils.db_commands.accounts import get_account_data
from utils.db_commands.users import get_user, update_chat_suggested, get_user_data
from main.config import CHANNEL_ID


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def on_new_chat_member(message: types.Message):
    friend_id = message.new_chat_members[0].id
    user_id = message.from_user.id

    if int(message.chat.id) == CHANNEL_ID:
        if await get_user(user_id):
            if not await get_user(friend_id):
                chat_suggested = await get_user_data(chat_id=user_id)
                if isinstance(chat_suggested, dict) and "chat_suggested" in chat_suggested:
                    chat_suggested_value = chat_suggested["chat_suggested"]

                    if isinstance(chat_suggested_value, int) and chat_suggested_value % 29 == 0:
                        account_data = await get_account_data(message.date)
                        if account_data:
                            if isinstance(account_data, dict):
                                update_result = await update_chat_suggested(chat_id=user_id, date=message.date)
                                if update_result:
                                    chat_text = "🎉 Siz account yutib oldingiz! Account ma'lumotlari sizga bot orqali yuborildi. Botni tekshiring."
                                    bot_text = (
                                        f"🎉 Tebriklaymiz! {chat_suggested_value} ta foydalanuvchi qo'shganingiz uchun tekin account yutib oldingiz!\n"
                                        f"📧 Email: {account_data.get('email')}\n"
                                        f"🔐 Parol: {account_data.get('password')}"
                                    )
                                    await message.answer(text=chat_text)
                                    await bot.send_message(user_id, text=bot_text)
                                else:
                                    error_text = "❌ Ball qo'shishda xatolik yuz berdi. Biz bilan bog'laning."
                                    await message.answer(text=error_text)
                            else:
                                error_text = "❌ Bizda muamo chiqdi , biz bilan bog'laning"
                                await message.answer(text=error_text)
                        else:
                            error_text = "❌ Bizda tekin account tugabdi. Account qo'shilib bo'lgandan keyin 1 ta odam qo'shsangiz, account olasiz."
                            await message.answer(text=error_text)
                    else:
                        text = "🎯 Sizning ballaringiz yangilandi! +1 Ball qo'shildi."
                        await message.answer(text=text)
                else:
                    error_text = "❌ Sizga ball qo'shilmadi. Ehtimol, botga kirib /start komandasini bajarish kerak."
                    await message.answer(text=error_text)
            else:
                error_text = "❌ Siz qo'shgan foydalanuvchi bizda allaqachon mavjud."
                await message.answer(text=error_text)
        else:
            error_text = (
                "❌ Siz qo'shgan odam hisoblanmaydi. Avval bizning botimizga kirib, /start komandasini bajaring.\n"
                "@studio_chat_group_bot -> Bizning botimiz")
            await message.answer(text=error_text)
    else:
        error_text = "❌ Bu bot faqat bizning guruhimizda ishlaydi."
        await message.answer(text=error_text)

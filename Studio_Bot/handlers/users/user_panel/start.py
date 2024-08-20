from aiogram import types
from keyboards.default.user import user_main_menu_def
from loader import dp
from main.config import CHANNEL_ID
from utils.db_commands.accounts import get_account_data
from utils.db_commands.users import update_bot_suggested, get_user, add_user, get_user_data


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    args = message.get_args()
    user_id = int(message.chat.id)

    existing_user = await get_user(user_id)
    if not int(message.chat.id) == CHANNEL_ID:
        if not existing_user:
            if await add_user(message):
                if args:
                    friend_id = int(args)
                    if friend_id != user_id:
                        await update_bot_suggested(chat_id=friend_id, date=message.date)
                        bot_suggested = await get_user_data(chat_id=friend_id)

                        if isinstance(bot_suggested, dict) and "bot_suggested" in bot_suggested:
                            bot_suggested_value = bot_suggested["bot_suggested"]

                            if isinstance(bot_suggested_value, int) and bot_suggested_value % 29 == 0:
                                account_data = await get_account_data(message.date)
                                user_text = "🎯 Do'stingizga ball qo'shildi!"
                                friend_text = (
                                    f"🎉 Tebriklaymiz! {bot_suggested_value} ta foydalanuvchi qo'shganingiz uchun tekin akkount yutib oldingiz!\n"
                                    f"📧 Email: {account_data['email']}\n"
                                    f"🔐 Parol: {account_data['password']}")
                                await message.answer(text=user_text)
                                await dp.bot.send_message(chat_id=friend_id, text=friend_text)
                            else:
                                user_text = "🎯 Sizning ballaringiz yangilandi!"
                                friend_text = "🎯 +1 Ball qo'shildi!"
                                await message.answer(text=user_text)
                                await dp.bot.send_message(chat_id=friend_id, text=friend_text)
                        else:
                            error_text = "❌ Referral ma'lumotlarida xatolik mavjud."
                            await message.answer(text=error_text, reply_markup=await user_main_menu_def())
                    else:
                        text = "❌ O'zingizni referral havolangizdan foydalanib ball qo'sha olmaysiz."
                        await message.answer(text=text)
                else:
                    await message.reply("👋 Xush kelibsiz! Biz bilan bog'laning va ball to'plang!",
                                        reply_markup=await user_main_menu_def())
            else:
                error_text = "❌ Foydalanuvchini qo'shishda xatolik yuz berdi. Iltimos, biz bilan bog'laning."
                await message.answer(text=error_text)
        else:
            if args:
                referrer_id = int(args)
                if referrer_id == user_id:
                    text = "❌ O'zingizni referral havolangizdan foydalanib ball qo'sha olmaysiz."
                    await message.answer(text=text)
                else:
                    text = "🎯 Siz bizda allaqachon mavjud foydalanuvchi bo'lganingiz uchun ball qo'shilmaydi."
                    await message.answer(text=text)
            else:
                text = "👋 Xush kelibsiz! Siz bizda allaqachon mavjud foydalanuvchi bo'lib turibsiz."
                await message.reply(text=text, reply_markup=await user_main_menu_def())
    else:
        pass


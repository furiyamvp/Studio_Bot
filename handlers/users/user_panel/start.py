from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.user import user_main_menu_def
from loader import dp, bot
from utils.db_commands.accounts import get_account_data
from utils.db_commands.users import get_user, get_user_data, update_suggested, add_user, update_suggested_to_zero


@dp.message_handler(CommandStart())
async def send_welcome(message: types.Message):
    args = message.get_args()
    user_id = int(message.chat.id)

    if await get_user(chat_id=user_id):
        if args:
            if await get_user(chat_id=int(args)):
                if user_id != int(args):
                    update_result = await update_suggested(chat_id=int(args), date=message.date)
                    suggested = await get_user_data(chat_id=int(args))

                    if isinstance(suggested, dict) and "suggested" in suggested:
                        suggested_value = suggested["suggested"]

                        if isinstance(suggested_value, int) and suggested_value % 20 == 0:
                            account_data = await get_account_data(message.date)
                            if account_data and isinstance(account_data, dict):
                                if update_result:
                                    friend_text = "🎉 Do'stingiz account yutib oldi"
                                    bot_text = (
                                        f"🎉 Tebriklaymiz! {suggested_value} ta foydalanuvchi qo'shganingiz uchun tekin account yutib oldingiz!\n"
                                        f"📧 Email: {account_data.get('email')}\n"
                                        f"🔐 Parol: {account_data.get('password')}"
                                    )
                                    await update_suggested_to_zero(chat_id=int(args), date=message.date)
                                    await message.answer(text=friend_text)
                                    await bot.send_message(args, text=bot_text)
                                else:
                                    error_text = "❌ Ball qo'shishda xatolik yuz berdi. Biz bilan bog'laning."
                                    await message.answer(text=error_text)
                            else:
                                error_text = "⚠️ Bizda tekin account tugabdi. Account qo'shilib bo'lgandan keyin 1 ta odam qo'shsangiz, account olasiz."
                                await message.answer(text=error_text)
                        else:
                            friend_text = "🎯 Sizga +1 ball qo'shildi"
                            user_text = "🎯 Do'stingizga ball qo'shildi +1"
                            await message.answer(text=user_text)
                            await bot.send_message(text=friend_text, chat_id=args)
                    else:
                        error_text = "❌ Referral ma'lumotlarida xatolik mavjud."
                        await message.answer(text=error_text, reply_markup=await user_main_menu_def())
                else:
                    error_text = "❌ O'zingizning referral havolangizdan foydalana olmaysiz."
                    await message.answer(text=error_text)
            else:
                error_text = "❌ Siz o'tgan link xato ekan, hech kimga ball berilmaydi."
                await message.answer(text=error_text)
        else:
            text = "👋 Xush kelibsiz!"
            await message.reply(text=text, reply_markup=await user_main_menu_def())
    else:
        if await add_user(message=message):
            if args:
                error_text = "⚠️ Siz bizda oldindan bor bo'lganingiz uchun do'stingizga ball berilmaydi."
                await message.answer(text=error_text)
            else:
                text = "👋 Xush kelibsiz!"
                await message.reply(text=text, reply_markup=await user_main_menu_def())
        else:
            text = "User qo'shishda xatolik yuz berdi"
            await message.reply(text=text, reply_markup=await user_main_menu_def())

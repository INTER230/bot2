from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton('Подпишись', url='https://t.me/music_from2023')
ikb.add(ib1)


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: return False

@dp.message_handler()
async def send_message_chat(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id='@music_from2023', user_id=message.from_user.id)):
            pass
    else: 
        await message.delete()
        await bot.send_message(message.chat.id, text=message.from_user.first_name + ', подпишитесь на канал: @music_from2023 чтобы писать сообщения в чат', reply_markup=ikb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, you are welcome') # Обработка команды /stat

@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file.id)

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('What are you talking about? I dont understand') # Обработка обычного сообщения

if __name__ == '__main__':
    executor.start_polling(dp)
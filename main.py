from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMRZPYXr77Jk5to1OxT7IR1tXHedTYAAmkbAALDlFlKR65n-ZmadxIwBA')
    await message.answer(f'{message.from_user.first_name}, you are welcome')  # Обработка команды /stat


@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)
    # бот будет отправлять мне в личные сообщения ID группы
    # с которой было отправлено это сообщение

@dp.message_handler(content_types=['document', 'photo']) # обработчик документов и фото
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('What are you talking about? I dont understand')  # Обработка обычного сообщения


if __name__ == '__main__':
    executor.start_polling(dp)

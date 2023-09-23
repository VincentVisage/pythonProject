from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import state
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv
from app import database as db
from app import keyboard as kb
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

async def on_startup(_):
    await db.db_start()
    print("Бот был успешно запущен")

class NewOrder(StatesGroup):
    type = (State)
    name = (State)
    desc = (State)
    price = (State)
    photo = (State)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMpZBAAAfUO9xqQuhom1S8wBMW98ausAAI4CwACTuSZSzKxR9LZT4zQLwQ')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в магазин кроссовок!',
                         reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=kb.main_admin)


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')


@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст',  reply_markup=kb.catalog_list)


@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста!')


@dp.message_handler(text='Контакты')
async def conttacts(message: types.Message):
    await message.answer(f'Покупать товар у него: @mesudoteach')


@dp.message_handler(text='Админ-панель')
async def contacts(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ-панель', reply_markup=kb.admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')


@dp.message_handler(text='Добавить товар')
async def add_item(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await NewOrder.type.set()
        await message.answer('Выберете тип товара', reply_markup=kb.catalog_list)
    else:
        await message.reply('Я тебя не понимаю.')

@dp.callback_query_handler(state=NewOrder.type)
async def add_item_type(call: types.CallbackQuery, FSMContext):
    async with state.proxy() as data:
        data['type'] = call.data
    await call.message.answer(f'Напишите название товара', reply_markup=kb.cancel)

@dp.callback_query_handler(state=NewOrder.name)
async def add_item_type(call: types.CallbackQuery, FSMContext):
    async with state.proxy() as data:
        data['name'] = call.data
    await call.message.answer(f'Дайте название товару', reply_markup=kb.cancel)

@dp.callback_query_handler(state=NewOrder.desc)
async def add_item_type(call: types.CallbackQuery, FSMContext):
    async with state.proxy() as data:
        data['desc'] = call.data
    await call.message.answer(f'Описание товара', reply_markup=kb.cancel)

@dp.callback_query_handler(state=NewOrder.price)
async def add_item_type(call: types.CallbackQuery, FSMContext):
    async with state.proxy() as data:
        data['price'] = call.data
    await call.message.answer(f'Цена товара', reply_markup=kb.cancel)


@dp.message_handler(lambda message: not message.photo, state=NewOrder.type)
async def add_item_photo_check(message: types.Message):
    await message.answer('Это не фото')

@dp.callback_query_handler(state=NewOrder.photo)
async def add_item_type(call: types.CallbackQuery, FSMContext):
    async with state.proxy() as data:
        data['photo'] = call.data
    await call.message.answer(f'Товар цспешно создан', reply_markup=kb.cancel)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю!.')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup )
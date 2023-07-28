from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import CallbackQuery


from keyboard_handlers import *
from inline_handlers import *
from text_handlers import *
from sqlite import *
from default_commands import *


import time
import datetime as dt
import random
import os
import dotenv
import asyncio


dotenv.load_dotenv()
token = os.getenv('API_TOKEN')
admin = int(os.getenv('ADMIN'))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text="Заебала эта хуета",
                         reply_markup=get_contact(),
                         parse_mode=pm)


@dp.message_handler()
async def messages_handler(message: types.Message):
    message.text = message.text.lower().strip()
    if message.text == 'github':
        await message.answer(text="`christmas-fire` [Ссылка](https://github.com/christmas-fire)",
                             disable_web_page_preview=True,
                             parse_mode=pm,
                             reply_markup=get_cancel())
    elif message.text in ('отменить', 'назад', 'вернуться в меню'):
        await message.answer(text=f'Команда "{message.text}" успешно выполнена!',
                             reply_markup=get_contact())
    elif message.text == 'телефон':
        await message.answer(text='`+79137477259`',
                             parse_mode=pm,
                             reply_markup=get_cancel())
    elif message.text == 'email':
        await message.answer(text='`vpiskin335@gmail.com`',
                             parse_mode=pm,
                             reply_markup=get_cancel())
    elif message.text == 'telegram':
        await message.answer(text='`christmas_fire` [Ссылка](https://t.me/christmas_fire)',
                             disable_web_page_preview=True,
                             parse_mode=pm,
                             reply_markup=get_cancel())
    elif message.text == 'avito':
        await message.answer(text='`Александр` [Ссылка](https://www.avito.ru/profile)',
                             disable_web_page_preview=True,
                             parse_mode=pm,
                             reply_markup=get_cancel())


async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


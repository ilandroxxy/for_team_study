# region import-ы
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import Text

import keyboard_handlers
from inline_handlers import *
from keyboard_handlers import *
from default_commands import *
from texts_for_users import *
from sqlite import *

import asyncio
import os
import random
import time
from dotenv import load_dotenv

pm: str = 'HTML'

load_dotenv()
token = os.getenv('TOKEN_API')
#admin = int(os.getenv('ADMIN'))

bot = Bot(token, parse_mode=pm)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я был запущен!')
    await db_start()
# endregion import-ы



@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    hello = ('Привет', 'Доброго времени суток', 'Приветствую Вас')
    await message.answer(text=ForUsers.push_command_start(message))




async def main():
    await set_bot_commands(bot)

    await dp.start_polling(
        bot)


if __name__ == '__main__':
    asyncio.run(main())

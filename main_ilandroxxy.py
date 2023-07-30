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
admin = int(os.getenv('ADMIN'))

bot = Bot(token, parse_mode=pm)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я был запущен!')
    await db_start()
# endregion import-ы



'''
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text=ForCommands.push_start_command(message),
                         reply_markup=keyboard_handlers.get_keyboard())
    await add_user(user_id=message.chat.id,
                   user_username=message.from_user.username,
                   user_first_name=message.from_user.first_name,
                   user_last_name=message.from_user.last_name)


@dp.message_handler(commands=["homework"])
async def homework_command(message: types.Message):
    await message.answer(text=ForCommands.push_homework_command(message),
                         parse_mode="HTML",
                         reply_markup=get_homework())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def handlers_for_callbacks(call: types.CallbackQuery):
    if call.data == "example":
        pass
'''


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text=ForUsers.push_command_start(message))
    else:
        hello = ('Привет', 'Доброго времени суток', 'Приветствую Вас')
        await message.answer(text=ForUsers.push_command_start(message))
        await bot.send_message(chat_id=admin,
                               text=f'#newuser: @{message.from_user.username}\n'
                                    f'ID: {message.chat.id}\n'
                                    f'[Написать сообщение](tg://user?id={message.chat.id})')


async def main():
    await set_bot_commands(bot)

    await dp.start_polling(
        bot)


if __name__ == '__main__':
    asyncio.run(main())

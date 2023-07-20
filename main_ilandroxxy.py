# region import-ы
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import Text

import keyboard_handlers
from inline_handlers import *
from keyboard_handlers import *
from texts_for_users import *
from sqlite import *

import os
import random
import time
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_API')

bot = Bot(token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я был запущен!')
    await db_start()
# endregion import-ы


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


@dp.message_handler()
async def message_handlers(message: types.Message):
    message.text = message.text.lower().strip()
    if message.text == 'random emoji':
        await message.answer(ForMessageHandlers.enter_message_random_emoji(message))



@dp.errors_handler(exception=BotBlocked)
async def error_bot_was_blocked(update: types.Update, exception: BotBlocked) -> bool:
    print(f"Кто-то заблокировал бота")
    return True


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

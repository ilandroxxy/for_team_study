# region import-ы
from aiogram import Bot, Dispatcher, executor, types

import asyncio
import os
import random
import dotenv

from default_commands import *
from texts_handlers import *
from inline_handlers import *

dotenv.load_dotenv()
token: str = os.getenv('TOKEN')
admin: int = int(os.getenv('ADMIN'))

bot = Bot(token)
dp = Dispatcher(bot)
pm: str = 'Markdown'
# endregion import-ы


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text=ForUser.push_command_start(message))


@dp.message_handler(commands=['getmyid'])  # todo прописать под каждую функцию и файл __doc__
async def command_getmyid(message: types.Message):
    """
    Команда /getmyid выводит пользователю его ID Telegram и позволяет переслать сообщение
    """
    await message.answer(text=ForUser.push_command_getmyid(message),
                         parse_mode=pm,
                         reply_markup=get_forward_id(message))

# todo Реализовать команду /help, которая заставит пользователей ввести обращение


@dp.message_handler()
async def messages_handlers(message: types.Message):
    get_message_text = message.text.lower().strip()

    if get_message_text == 'привет':
        await message.answer(text='Чо надо?')
        # todo: Перенести все текстики в файл text_handlers (распределить классы)

    elif any(x in get_message_text for x in ('#help', 'помогите', 'помог', 'help')):
        await message.answer(text='Я (бот) отправил сообщение модераторам, ожидайте ответа в ЛС')
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.send_help_forward(message, message.text))

    else:
        await message.answer(text=ForUser.push_trash(message))


async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



from aiogram import Bot, Dispatcher, executor, types
import os
from random import choice
from string import ascii_uppercase
from dotenv import load_dotenv

PARSE_MODE: str = 'HTML'
ALPHABET = ascii_uppercase

HELP_TEXT = """
/start - перезапустить бот
/help - список команд в боте
/description - описание бота
"""

load_dotenv()
token = os.getenv('TOKEN_API')

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Hello, World!")
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_TEXT)


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text="Пока что это просто учебный бот\n"
                              "Попробуем сделать что-то интересное.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(text=choice(ALPHABET))


if __name__ == '__main__':
    executor.start_polling(dp)

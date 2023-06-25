from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

HELP_TEXT = """
/start - перезапустить бот
/help - список команд в боте
"""

load_dotenv()
token = os.getenv('TOKEN_API')

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text="Hello, World!")
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_TEXT)


@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) >= 2:
        await message.answer(text=message.text.upper())
    else:
        await message.answer(text="Не удовлетсворяет условию")


if __name__ == '__main__':
    executor.start_polling(dp)

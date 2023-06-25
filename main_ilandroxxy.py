from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

PARSE_MODE: str = 'HTML'
COUNT = 0


load_dotenv()
token = os.getenv('TOKEN_API')

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global COUNT
    COUNT += 1
    await message.answer(text=f"Кол-во запусков: {COUNT}")


@dp.message_handler()
async def echo(message: types.Message):
    if "0" in message.text:
        await message.reply(text="YES")
    else:
        await message.reply(text='NO')


if __name__ == '__main__':
    executor.start_polling(dp)

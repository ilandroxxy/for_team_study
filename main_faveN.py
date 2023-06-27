import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
load_dotenv()
token = os.getenv('TOKEN')


bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) >= 2:
        await message.answer(text=message.text.upper())
    else:
        await message.answer(text="Не удовлетворяет условию")


if __name__ == '__main__':
    executor.start_polling(dp)


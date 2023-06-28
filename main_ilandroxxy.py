# region import-ы
from aiogram import Bot, Dispatcher, executor, types
from inline_handlers import links_buttons
from keyboard_handlers import kb
import os
import random
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_API')

bot = Bot(token)
dp = Dispatcher(bot)
# endregion import-ы


async def on_startup(_):
    print('Я был запущен!')


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}", reply_markup=kb)


@dp.message_handler(commands=["links"])
async def links_command(message: types.Message):
    await message.answer(text="Давайте решим рандомную задачку", reply_markup=links_buttons)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

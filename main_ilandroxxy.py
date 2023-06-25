# region import-ы
from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_API')

bot = Bot(token)
dp = Dispatcher(bot)
# endregion import-ы

PARSE_MODE: str = 'HTML'


async def on_startup(_):
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['give'])
async def count_command(message: types.Message):
    await message.answer(text="Смотри, какой смешной кодер 👾")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgQAAxkBAAEJeRlkmBvuHYXoPXPqA1ZaRA6XpZuTngACUAEAAqghIQaxvfG1zemEoi8E")


@dp.message_handler()
async def echo_emoji(message: types.Message):
    if message.text == "❤️":
        await message.reply(text="🖤")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

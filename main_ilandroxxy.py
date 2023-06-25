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
HELP_TEXT = """
<b>/start</b> - <em>перезапустить бота</em> 
<b>/help</b> - <em>вывести список команд</em>
"""

async def on_startup(_):
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_TEXT, parse_mode="HTML")


@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=54.858393,
                            longitude=83.110603)


@dp.message_handler()
async def echo_emoji(message: types.Message):
    await message.reply(text=f"В твоем сообщение {message.text.count('✅')} символов ✅.")


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
     await message.answer(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

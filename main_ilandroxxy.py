# region import-ы
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
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

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = KeyboardButton("/help")
btn2 = KeyboardButton("/description")
btn3 = KeyboardButton("❤️")
kb.add(btn1, btn2)


async def on_startup(_):
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_TEXT, parse_mode="HTML", reply_markup=kb)


@dp.message_handler(commands=['clear'])
async def clear_command(message: types.Message):
    await bot.send_message(message.chat.id, text="Удалил кнопки", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['getmyid'])
async def getmyid_command(message: types.Message):
    await bot.send_message(message.chat.id, text=f"Ваш id: {message.chat.id}")


@dp.message_handler(commands=['order'])
async def order_command(message: types.Message):
    if message.chat.id == 438879394:
        await message.answer(text="Ты даун, зачем заказал сам у себя!")
    else:
        await bot.send_message(438879394, text=f"Был оформлен заказ: {message.chat.id}")
        await message.answer(text="Заказ успешно отправлен!")
        await message.delete()
        await bot.send_sticker(message.chat.id, sticker="CAACAgQAAxkBAAEJeRlkmBvuHYXoPXPqA1ZaRA6XpZuTngACUAEAAqghIQaxvfG1zemEoi8E")



@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=54.858393,
                            longitude=83.110603)


@dp.message_handler()
async def echo_emoji(message: types.Message):
    if message.text == "❤️":
        await bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEJgENkmw_PBJxS83dlUsd_TtPiZFfRWgACERQAAqAAAehLhynfNnamXaEvBA")
    else:
        await message.reply(text=f"В твоем сообщение {message.text.count('✅')} символов ✅.")


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
     await message.answer(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

# region import-ы
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from inline_handlers import photo_buttons, get_inline_keyboard
from keyboard_handlers import kb, kb_send_photo
from texts_for_users import for_picture

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
# endregion import-ы

number = {}




@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    number[message.chat.id] = 0
    await message.answer(f'The current number is: {number[message.chat.id]}',
                         reply_markup=get_inline_keyboard())



@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def handlers_for_callbacks(call: types.CallbackQuery):
    global number
    if call.data == "btn_increase":
        number[call.message.chat.id] += 1
        await call.message.edit_text(f'The current number is: {number[call.message.chat.id]}',
                                     reply_markup=get_inline_keyboard())
    elif call.data == "btn_decrease":
        number[call.message.chat.id] -= 1
        await call.message.edit_text(f'The current number is: {number[call.message.chat.id]}',
                                     reply_markup=get_inline_keyboard())
    elif call.data == 'btn_random':
        number[call.message.chat.id] = random.randint(-1000, 1000)
        await call.message.edit_text(f'The current number is: {number[call.message.chat.id]}',
                                     reply_markup=get_inline_keyboard())



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

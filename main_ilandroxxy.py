# region import-ы
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from inline_handlers import photo_buttons
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

dict_voted_users = {}

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo="https://ru.freepik.com/premium-photo/portrait-of-male-programmer-in-office_13708354.htm",
                         caption=for_picture.text_for_test_picture,
                         reply_markup=photo_buttons)



@dp.callback_query_handler()
async def handlers_for_callbacks(call: types.CallbackQuery):
    if call.data == "close_photo_buttons":
        await call.message.delete()
    if call.message.chat.id not in dict_voted_users:
        if call.data == "like_photo_buttons":
            await call.answer(show_alert=False, text=f"{str(call.data)} понравилась картинка")
            dict_voted_users[call.message.chat.id] = "👍"
        elif call.data == "dislike_photo_buttons":
            await call.answer(show_alert=False, text=f"{str(call.data)} не понравилась картинка")
            dict_voted_users[call.message.chat.id] = "👎"
    else:
        await call.answer(text=f"Ты уже голосовал {dict_voted_users[call.message.chat.id]}",
                          show_alert=True)



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

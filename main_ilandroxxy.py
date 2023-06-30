# region import-ы
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from inline_handlers import links_buttons, contact_buttons
from keyboard_handlers import kb, kb_send_photo

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

@dp.message_handler(commands=["Venya"])
async def Venya_coommand(message: types.Message):
    await message.answer(text="<b>Веня</b>, мы тебя услышали", parse_mode='HTML')
    await bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEJhmBknVKv0Thaglc40AabNwk4rLRQ9gAC_wEAApfYKgz93kVX-B64Pi8E")
    await message.delete()



@dp.message_handler(Text(equals='Рандомная картинка'))
async def open_keyboard_photo(message: types.Message):
    await message.answer(text="Чтобы отправить рандомную фотографию нажми на кнопку Рандом",
                         reply_markup=kb_send_photo)


@dp.message_handler()
async def echo_answer(message: types.Message):
    if message.text == 'Контакты':
        await bot.send_message(message.chat.id, text="А вот нажми на кнопочку", reply_markup=contact_buttons)
    elif message.text == 'Главное меню':
        await message.answer(text='Открыл главное меню', reply_markup=kb_send_photo)
        await message.delete()


@dp.callback_query_handler()
async def test_callback(callback: types.CallbackQuery):
    if callback.data == "lessons":
        await callback.answer(text="Вот мои контакты")
    await callback.answer(text="Еще что-то")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

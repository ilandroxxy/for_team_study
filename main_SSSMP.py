# region import-ы
import types

from aiogram import Bot, Dispatcher, executor, types

import asyncio
import os
import random
import dotenv

from default_commands import *
from texts_handlers import *
from i_handlers import *

dotenv.load_dotenv()
token: str = os.getenv('TOKEN')
admin: int = int(os.getenv('ADMIN'))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'
# endregion import-ы


@dp.message_handler(commands=['start'])
async def command_start(messege: types.Message):
    await messege.answer(text=ForUser.push_command_start(messege))


@dp.message_handler(commands=['getmyid'])
async def command_getmyid(messege: types.Message):
    ikb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Vashemu repu',
                                     switch_inline_query=ForUser.push_command_getmyid(messege))
    ikb.add(btn)
    await messege.answer(text=ForUser.push_command_getmyid(messege),
                         parse_mode=pm,
                         reply_markup=get_forward_id(messege))


@dp.message_handler()
async def messege_handlers(messege: types.Message):
    get_messege_text = messege.text.lower().strip()

    if get_messege_text == 'Дарова':
        await messege.answer(text='Dota2')

    elif any(x in get_messege_text for x in ('#help', 'pamagi', 'nado ochen')):
        await messege.answer(text='Admin uvedomlen')
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.send_help_self(messege, messege.text))


    else:
        await messege.answer(text=ForUser.push_trash(messege))


async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



#to_do
# перенести все тексты в файл text_handlers
# реализовать команду /help (Введите ваше обращение, пользователь вводит, увед пользователю и админу)
# Во всех функциях и файлах прописать комменты


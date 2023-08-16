"""В этом файле хранится само тело бота и большинство переменных"""


# region import-ы
import types

from aiogram import Bot, Dispatcher, executor, types

import asyncio
import os
import random
import dotenv

from keyboard_handlers import *
from default_commands import *
from texts_handlers import *
from i_handlers import *

dotenv.load_dotenv()
token: str = os.getenv('TOKEN')
admin: int = int(os.getenv('ADMIN'))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'
HELP_HANDLERS = {}
# endregion import-ы

"""Реализация команды /start"""
@dp.message_handler(commands=['start'])
async def command_start(messege: types.Message):
    await messege.answer(text=ForUser.push_command_start(messege),
                         reply_markup=get_kb_start_menu())
    await messege.delete()

"""Реализация команды /getmyid"""
@dp.message_handler(commands=['getmyid'])
async def command_getmyid(messege: types.Message):
    ikb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text=ForUser.push_ikbtext_getmyid(messege),
                                     switch_inline_query=ForUser.push_command_getmyid(messege))
    ikb.add(btn)
    await messege.answer(text=ForUser.push_command_getmyid(messege),
                         parse_mode=pm,
                         reply_markup=get_forward_id(messege))
    await messege.delete()

"""Реализация команды /help + попытался реализовать свою идею"""
@dp.message_handler(commands=['help'])
async def command_help(messege: types.Message):
    HELP_HANDLERS[messege.chat.id] = 'help'
    await messege.answer(text=ForUser.push_text_toadmin(messege))
    # await messege.answer(text=ForUser.push_command_help(messege)) -- ВЫДЕЛИТЬ В ОТДЕЛЬНУЮ КОМАНДУ
    await messege.delete()


@dp.message_handler(commands=['contact'])
async def command_contact_github(messege: types.Message):
    await bot.send_photo(chat_id=messege.chat.id, photo=open('photo/rayan.jpg', 'rb'),
                         caption=ForUser.push_command_contact(messege),
                         parse_mode=pm,
                         reply_markup=get_contact_github(messege))
    await bot.send_media_group(chat_id=messege.chat.id, media=[types.InputMediaPhoto(open('photo/rayan.jpg', 'rb'),
                                                                                     caption='фотка 1'),
                                                               types.InputMediaPhoto(open('photo/rayan.jpg', 'rb'),
                                                                                     caption='фотка 2')])
    await messege.delete()


@dp.message_handler(commands=['stickers'])
async def command_contact_stickers(messege: types.Message):
    sticker = ('CAACAgIAAxkBAAEKCuBk3MOEIvfZ691ODqq1guylXXZL-AACzB4AAjQ0yUhuU6hqMftC7TAE',
                'CAACAgIAAxkBAAEKCuJk3MOah3v2RRaTSFOG3hJGzc8bhAACCCEAAgcByUi7KKdfGD18NTAE',
                'CAACAgIAAxkBAAEKCuRk3MOeLqPTDXZC28lIfBPRMhmKeQACwSAAArwM-Emqykozbwy4jTAE')
    await bot.send_sticker(chat_id=messege.chat.id, sticker=random.choice(sticker))





"""Реализация ответа на какой-то бред от пользователя + ответ на ключевое слово"""
@dp.message_handler()
async def messege_handlers(messege: types.Message):
    get_messege_text = messege.text.lower().strip()

    if get_messege_text == ForUser.get_messege_text(messege):
        await messege.answer(text=ForUser.messege_answer(messege))

    elif any(x in get_messege_text for x in ForUser.get_trash(messege)):
        await messege.answer(text=ForUser.push_text_help(messege))
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.send_help_self(messege, messege.text))

    elif get_messege_text == 'обратная связь':
        await messege.answer(text='обработал')

    elif get_messege_text == 'контакты':
        await bot.send_photo(chat_id=messege.chat.id, photo=open('photo/rayan.jpg', 'rb'),
                             caption=ForUser.push_command_contact(messege),
                             parse_mode=pm,
                             reply_markup=get_contact_github(messege))

    else:
        if HELP_HANDLERS.get(messege.chat.id) == 'help':
            HELP_HANDLERS[messege.chat.id] = 0
            await bot.send_message(chat_id=admin, text=ForUser.help_handlers(messege, messege.text))
            await messege.answer(text='Ваше сообщение доставлено')
        else:
            await messege.answer(text=ForUser.push_trash(messege))





async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



#to_do
# перенести все тексты в файл text_handlers +
# реализовать команду /help (Введите ваше обращение, пользователь вводит, увед пользователю и админу) +
# Во всех функциях и файлах прописать комменты +



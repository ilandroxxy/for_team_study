from aiogram import Bot, executor, Dispatcher, types


import asyncio
import os
import dotenv
import random

from defaut_commands import *
from text_handlers import *
from i_handlers import *

dotenv.load_dotenv()
token: str = os.getenv('TOKEN_API')
admin: int = int(os.getenv('ADMIN'))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'

# async def on_startup(_):
#     print('Бот успешно запущен!')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text=ForUser.push_command_start(message))


@dp.message_handler(commands=['getmyid']) #todo прописать под каждую функцию и файл __doc__
async def command_getmyid(message: types.Message):
    await message.answer(text=ForUser.push_command_getmyid(message),
                         parse_mode=pm,
                         reply_markup=get_forward_id(message))

#todo реализовать кнопку /help(введите че вы хотите)

@dp.message_handler()
async def messages_handlers(message: types.Message):
    get_message_text = message.text.lower().strip()
    if get_message_text == 'привет':
        await message.answer(text='Ну здравствуй')
        #todo: перенести все тексты в text_hand

    elif any(x in get_message_text for x in ('#help', 'помогите', 'help', 'как оплатить')):
        await message.answer(text='Отправил сообщение модераторам')
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.send_help_self(message, message.text))

    else:
        await message.answer(text=ForUser.push_trash(message))




async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



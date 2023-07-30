from aiogram import Dispatcher, Bot, executor, types

import asyncio
from dotenv import load_dotenv

import os
import random

from default_commands import *
from Inline_handlers import *
from Reply_handlers import *
from texts_for_bot import *


load_dotenv()
token = os.getenv('API_TOKEN')
admin = int(os.getenv('ADMIN'))
group = int(os.getenv('GROUP'))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'
emojis = "😅🙏😂😭😄😢😍❤️😁👍☺️😱😌🥳😎👾🤖💙💚💫💥💣💯💭👈👉👇"

async def on_startup(_):
    print('Я запустился')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text=f'Доброго времени суток, {message.from_user.first_name} \n'
                                  f'Ваш id: `{message.chat.id}`',
                             parse_mode=pm,
                             reply_markup=start_buttons())
        await message.delete()
    else:
        await message.answer(text=f'Доброго времени суток, {message.from_user.first_name} \n'
                                  f'Ваш id: `{message.chat.id}`',
                             parse_mode=pm)
        await message.delete()
        await bot.send_message(chat_id=admin,
                               text=f'#newuser @{message.from_user.username} \n'
                                    f'id: `{message.chat.id}` \n'
                                    f'[Написать сообщение](tg://user?id={message.chat.id})',
                               parse_mode=pm)


@dp.message_handler()
async def messages_handler(message: types.Message):
    message.text = message.text.lower().strip()
    if message.text == 'контакты' or message.text == '/getcontacts':
        await message.answer(text=contacts_text(),
                             parse_mode=pm,
                             disable_web_page_preview=True,
                             reply_markup=my_contacts_buttons())
    elif message.text == 'записаться на урок':
        await message.answer(text=sign_lesson_text(),
                             reply_markup=write_to_me())


@dp.callback_query_handler()
async def callbacks_handler(call: types.CallbackQuery):
    if call.data == "11":
        await call.message.answer(random.choice(emojis))


async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


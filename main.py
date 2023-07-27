from aiogram import Dispatcher, Bot, executor, types

import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('API_TOKEN')
admin = int(os.getenv('ADMIN'))
group = int(os.getenv('GROUP'))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'


async def on_startup(_):
    print('Я запустился')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text=f'Доброго времени суток, {message.from_user.first_name} \n'
                                  f'Ваш id: `{message.chat.id}`',
                             parse_mode=pm)
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
async def echo_bot(message: types.Message):
    if len(message.text.split()) > 3:
        await message.answer(text=message.text)
    else:
        await message.answer(text=f'не подходит')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)


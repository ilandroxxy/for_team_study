from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "5734914555:AAETPQsfcDp2H7XJVJfdqpnvpVeMrLLmNso"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) >= 2:
        await message.answer(text=message.text.upper())
    else:
        await message.answer(text="Не удовлетсворяет условию")


if __name__ == '__main__':
    executor.start_polling(dp)

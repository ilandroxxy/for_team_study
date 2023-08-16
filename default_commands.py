from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    custom_commands = [
        BotCommand(command="start", description="Перезапуск бота, на стартовую позицию 🏁"),
        BotCommand(command="help", description="Техподдержка, 123 напишите нам ⚙️"),
        BotCommand(command="getmyid", description="Бот покажет ваш id пользователя Telegram 👾"),
        BotCommand(command="contact", description="Мои контакты!"),
        BotCommand(command='stickers', description="Получите стикеры!")
    ]

    await bot.set_my_commands(
        commands=custom_commands, scope=BotCommandScopeAllPrivateChats()
    )
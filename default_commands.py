from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    custom_commands = [
        BotCommand(command="start", description="Перезапуск бота, на стартовую позицию 🏁"),
        BotCommand(command="getcontacts", description="Мои контакты👾"),
        BotCommand(command='homework', description='Сдать домашку')
    ]

    await bot.set_my_commands(
        commands=custom_commands, scope=BotCommandScopeAllPrivateChats()
    )
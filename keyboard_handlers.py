import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_contact() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(text="GitHub"),
        KeyboardButton(text="Телефон", url="+79137477259"),
        KeyboardButton(text="Email", url="vpiskin335@gmail.com"),
        KeyboardButton(text="Telegram", url="https://t.me/christmas_fire"),
        KeyboardButton(text="Avito", url="https://www.avito.ru/profile")
    )
    return keyboard


def get_cancel() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(text="Отменить"),
    )
    return keyboard



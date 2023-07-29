from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_buttons() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(
        KeyboardButton(text='Контакты'),
        KeyboardButton(text='Записаться на урок')
    )
    return rkm
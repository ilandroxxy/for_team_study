from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_kb_start_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton('Обратная связь'),
        KeyboardButton('Контакты')
    )
    return kb
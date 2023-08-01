from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def write_to_me() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Мой аккаунт", url='https://t.me/honicraft')
        ]
    ])
    return ikb


def my_contacts_buttons() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Мой аккаунт", url='https://t.me/honicraft'),
            InlineKeyboardButton(text="Мой авито", url='https://clck.ru/359D5t')
        ]
    ])
    return ikb


def homework_buttons() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Задачи ЕГЭ", callback_data='EGE_zadachi'),
            InlineKeyboardButton(text="Теория Питона", callback_data='Python_Theory'),
            InlineKeyboardButton(text="Сдать домашку", callback_data='get_homework')
        ]
    ])
    return ikb
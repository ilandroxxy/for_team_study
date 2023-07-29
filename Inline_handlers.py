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
            InlineKeyboardButton(text="Мой авито", url='https://www.avito.ru/moskva/predlozheniya_uslug/repetitor_k_egeoge_po_informatike_3315329905')
        ]
    ])
    return ikb
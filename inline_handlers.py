from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from texts_handlers import *


def get_forward_id(mess) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Отправьте вашему репетитору',
                                 switch_inline_query=ForUser.push_command_getmyid(mess))
        ]
    ])
    return ikb


'''
def get_contact() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='GitHub', url='https://github.com/ilandroxxy'),
            InlineKeyboardButton(text='Telegram', url='t.me/ilandroxxy')
        ]
    ])
    return ikb
'''

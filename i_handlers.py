from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from text_handlers import *
'''
def get_contact() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        InlineKeyboardButton(text='GitHub', url='https://github.com/Grimstrou'),
        InlineKeyboardButton(text='Telegram', url='t.me/Grimstrou')
    ])
    return ikb
'''


def get_forward_id(mess) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Отправьте вашему репетитору',
                             switch_inline_query=ForUser.push_command_getmyid(mess))
        ]
    ])
    return ikb

'''
ikb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Отправьте вашему репетитору',
                                     switch_inline_query=ForUser.push_command_getmyid(message))
    ikb.add(btn)
'''
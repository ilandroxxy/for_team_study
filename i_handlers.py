from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts_handlers import *

def get_forward_id(mess) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text='Vashemu repu',
                             switch_inline_query=ForUser.push_command_getmyid(mess))
        ]
    ])
    return ikb


'''
def get_contact() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text='GitHub', url='https://github.com/SMP1488'),
        InlineKeyboardButton(text='Tg', url='t.me/AnotherPumpkin'),
        ]
    ])
    return ikb
'''



'''
ikb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Vashemu repu',
                                     switch_inline_query=ForUser.push_command_getmyid(messege))
    ikb.add(btn)
'''
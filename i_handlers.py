"""В этом файле лежит кнопка пересылки айдишника админу"""


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts_handlers import *

def get_forward_id(mess) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text=ForUser.push_ikbtext_getmyid(mess),
                             switch_inline_query=ForUser.push_command_getmyid(mess))
        ]
    ])
    return ikb



def get_contact_github(mess) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text=ForUser.push_ikbtext_contact_github(mess), url='https://github.com/SMP1488'),
        InlineKeyboardButton(text=ForUser.push_ikbtext_contact_tg(mess), url='t.me/AnotherPumpkin')
        ]
    ])
    return ikb





'''
ikb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Vashemu repu',
                                     switch_inline_query=ForUser.push_command_getmyid(messege))
    ikb.add(btn)
'''
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
# emojis = "😅🙏😂😭😄😢😍❤️😁👍👎☺️😱😌🥳😎👾🤖💙💚💫💥💣💯💭👈👉👇"

photo_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("👍", callback_data="like_photo_buttons"), InlineKeyboardButton("👎", callback_data="dislike_photo_buttns")],
    [InlineKeyboardButton("Закрыть клавиатуру", callback_data='close_photo_buttons')]
])

def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase', callback_data='btn_increase'), InlineKeyboardButton('Decrease', callback_data='btn_decrease')],
        [InlineKeyboardButton('Random number', callback_data='btn_random')]
    ])
    return ikb


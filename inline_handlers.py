from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
# emojis = "😅🙏😂😭😄😢😍❤️😁👍👎☺️😱😌🥳😎👾🤖💙💚💫💥💣💯💭👈👉👇"

photo_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("👍", callback_data="like_photo_buttons"), InlineKeyboardButton("👎", callback_data="dislike_photo_buttns")],
    [InlineKeyboardButton("Закрыть клавиатуру", callback_data='close_photo_buttons')]
])




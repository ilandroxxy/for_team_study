from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# emojis = "😅🙏😂😭😄😢😍❤️😁👍👎☺️😱😌🥳😎👾🤖💙💚💫💥💣💯💭👈👉👇"


def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton('/start'),
        KeyboardButton('/homework'),
        KeyboardButton('random emoji')
    )
    return kb
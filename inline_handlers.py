from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
# emojis = "😅🙏😂😭😄😢😍❤️😁👍👎☺️😱😌🥳😎👾🤖💙💚💫💥💣💯💭👈👉👇"


HOMEWORK = ((),
            ('stepik.org/lesson/1038531/step/1',
             'stepik.org/lesson/1038532/step/1',
             'stepik.org/lesson/1038535/step/1'
             ),
            )


def get_homework() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', url=f"{random.choice(HOMEWORK[1])}"),
         InlineKeyboardButton('2', callback_data='geuir'),
         InlineKeyboardButton('3', callback_data='btn_hw_1'),
         InlineKeyboardButton('4', callback_data='btn_hw_1'),
         InlineKeyboardButton('5', callback_data='btn_hw_1')
         ],
        [InlineKeyboardButton('6', callback_data='btn_hw_1'),
         InlineKeyboardButton('7', callback_data='btn_hw_1'),
         InlineKeyboardButton('8', callback_data='btn_hw_1'),
         InlineKeyboardButton('9', callback_data='btn_hw_1'),
         InlineKeyboardButton('10', callback_data='btn_hw_1')
         ]
    ])
    return ikb




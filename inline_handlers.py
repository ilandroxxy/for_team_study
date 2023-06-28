from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

numbers14 = [11352, 48389, 48382, 48380, 48384]
numbers15 = [34515, 48463, 8666, 18630, 40731]

links_buttons = InlineKeyboardMarkup(row_width=1)
links_button1 = InlineKeyboardButton(text='Задачка 14-го номера', url=f"https://inf-ege.sdamgia.ru/problem?id={random.choice(numbers14)}")
links_button2 = InlineKeyboardButton(text='Задачка 15-го номера', url=f"https://inf-ege.sdamgia.ru/problem?id={random.choice(numbers15)}")
links_buttons.add(links_button1).add(links_button2)
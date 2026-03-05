from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests

link = "https://fakeapi.pythonanywhere.com/products/"
response = requests.get(url=link).json()

menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Menyu 🍕", callback_data='menyu'), InlineKeyboardButton(text="Bog'lanish", web_app=WebAppInfo(url="https://olcha.uz"))],
        [InlineKeyboardButton(text="Bog'lanish", callback_data='boglanish')]
    ]
)


def MenyuBot1():
    buttons = InlineKeyboardBuilder()
    for name in response:
        buttons.add(InlineKeyboardButton(text=name['title'], callback_data=name['title']))
    buttons.add(InlineKeyboardButton(text='ortga', callback_data="ortga"))
    buttons.adjust(2)
    return buttons.as_markup()



def Sonlar():
    buttons = InlineKeyboardBuilder()
    for name in range(1, 10):
        buttons.add(InlineKeyboardButton(text=f"{name}", callback_data=f"{name}"))
    buttons.add(InlineKeyboardButton(text='ortga', callback_data="ortga1"))
    buttons.adjust(3)
    return buttons.as_markup()
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder


information = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Contact ☎️", request_contact=True), KeyboardButton(text="Location", request_location=True)]
    ], resize_keyboard=True
)


menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menyu 🍕"), KeyboardButton(text="Biz haqimizda", web_app=WebAppInfo(url="https://olcha.uz/ru"))],
        [KeyboardButton(text="Bog'lanish")]
    ],
    resize_keyboard=True
)





def Maxsulotlar(menyu):
    buttons = ReplyKeyboardBuilder()
    for name in menyu:
        buttons.add(KeyboardButton(text=name['title']))
    buttons.adjust(2)
    return buttons.as_markup(resize_keyboard=True)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kino qoshish", callback_data='kino add', style="danger")],
        [InlineKeyboardButton(text="obunachilar", callback_data='obuna', style='success')]
    ]
)
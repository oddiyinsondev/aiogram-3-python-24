from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kino izla", callback_data='kino', style="danger"), InlineKeyboardButton(text="Google Translate", callback_data="tarjima", style="primary")],
        [InlineKeyboardButton(text="Wkipideia", callback_data='wki', style='success'), InlineKeyboardButton(text="Admin", callback_data='admin')]
    ]
)
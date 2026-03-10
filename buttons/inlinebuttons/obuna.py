from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

obuna_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Obuna bo'ling", url="https://t.me/rajabov_flow")],
        [InlineKeyboardButton(text="Tekshirish ✔", callback_data="tek")]
    ]
)
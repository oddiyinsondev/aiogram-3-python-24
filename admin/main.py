from aiogram.types import Message
from aiogram import Router, F
from config.config import admins
from buttons.inlinebuttons.admin_add import menu
admin_router = Router()

@admin_router.message(F.from_user.id.in_(admins) and F.text == "qoshish")
async def AdminsBot(message: Message):
    await message.answer("Assalomu alaykum nima qo'shamiz", reply_markup=menu)


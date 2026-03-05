from aiogram.types import Message
from aiogram import Router, F
from config.config import admins
from main import bot

rek_router = Router()

@rek_router.message(F.text == "admin", F.from_user.id.in_(admins))
async def ReklamaBot(message: Message):
    id = message.from_user.id
    await bot.send_message(chat_id=id, text="reklamar ketdi")
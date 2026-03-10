from aiogram.filters import Filter
from config.config import kanal_id
from aiogram import Bot
from aiogram.types import Message


class CheckSubChanel(Filter):
    async def __call__(self, message:Message, bot:Bot):
        user_status = await bot.get_chat_member(kanal_id, message.from_user.id)
        if user_status.status in ['administrator', 'creator', 'member']:
            return False
        else:
            return True
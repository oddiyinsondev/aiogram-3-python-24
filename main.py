import asyncio
import logging
from aiogram import Dispatcher, Bot
from config.config import Bot_token, admins
from handler.main1 import translate_router
from handler.start import start_router
from admin.main import admin_router
# from admin.reklama import rek_router


bot = Bot(token=Bot_token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


async def main():
    for admin in admins:
        await bot.send_message(chat_id=admin, text="bot ishladi")
    dp.include_router(admin_router)
    # dp.include_router(rek_router)
    dp.include_router(start_router)
    dp.include_router(translate_router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("tugadi")





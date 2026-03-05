import logging
import asyncio
from config import token
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters.command import CommandStart
from inline_buttons import menyu, MenyuBot1, Sonlar
import requests
import yt_dlp


link = "https://fakeapi.pythonanywhere.com/products/"
response = requests.get(url=link).json()

bot = Bot(token=token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

bazzam = [5933580972, 1813933302, 7072212883, 8531065156]

@dp.message(CommandStart())
async def StartBot(message: Message):
    user_id = message.from_user.id
    await message.answer(f"Assalomu alaykum Xush kelibsiz\n{message.from_user.full_name}", reply_markup=menyu)


@dp.callback_query(F.data == 'menyu')
async def MenyuBot(call: CallbackQuery):
    await call.message.answer(text="bot", reply_markup=MenyuBot1())
    await call.message.delete()


@dp.callback_query(F.data=='ortga')
async def Ortgabot(call: CallbackQuery):
    await call.answer("ortga keldingiz", show_alert=True)
    await call.message.answer(f"Maxsulotlar bo'limi\n{call.from_user.full_name}", reply_markup=menyu)
    await call.message.delete()


@dp.callback_query(F.data=='ortga1')
async def Ortgabot(call: CallbackQuery):
    await call.answer("ortga keldingiz", show_alert=True)
    await call.message.answer(f"Maxsulotlardan birini tanlang\n{call.from_user.full_name}", reply_markup=MenyuBot1())
    await call.message.delete()
    

@dp.callback_query(F.data)
async def Maxsulotbot(call: CallbackQuery):
    xabar = call.data
    if xabar.isdigit():
        await call.answer(text=f"{xabar} ta zakaz qilindi", show_alert=True)
    else:
        for name in response:
            if xabar == name['title']:
                if name['image']:
                    await call.message.answer_photo(photo=name['image'], caption=f"Nomi: {name['title']}\nNarxi: {name['summ']}", reply_markup=Sonlar())
                    await call.message.delete()
                else:
                    await call.message.answer(f"Nomi: {name['title']}\nNarxi: {name['summ']}", reply_markup=Sonlar())
                    await call.message.delete()
                break
        else:
            await call.answer("siz so'ragan maxsulot yoq", show_alert=True)
            await call.message.delete()
    # await call.message.answer()





    
    
async def main():
    await bot.send_message(chat_id=7072212883, text="bot isha tushdi")
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("tugadi")
    

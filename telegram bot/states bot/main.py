import logging
import asyncio
from  aiogram.types import Message
from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from config import Bot_token, kanal_id
from states import Hobby
from aiogram.fsm.context import FSMContext
from buttons import menyu


logging.basicConfig(level=logging.INFO)
bot = Bot(token=Bot_token)
dp = Dispatcher()

@dp.message(CommandStart())
async def Startbot(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum ismingizni kiriting ")
    await state.set_state(Hobby.name)

@dp.message(F.text, Hobby.name)
async def Namebot(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data({'ism':ism})
    await message.answer(f"Bot yasashga qiziqasizmi\n{ism}", reply_markup=menyu)
    await state.set_state(Hobby.hobby)
    
    
@dp.message(F.text, Hobby.hobby)
async def HobbyBot(message: Message, state: FSMContext):
    ha = message.text
    if ha.lower() == 'no':
        await message.answer("siz o'ta olmadingiz")
        await state.clear()
    else:
        await state.update_data(ha=ha)
        await message.answer("Qaysi dasturlash tilidan foydalanasiz")
        await state.set_state(Hobby.language)
    
@dp.message(F.text, Hobby.language)
async def LanguageBot(message: Message, state: FSMContext):
    language = message.text
    await state.update_data(language=language)
    data = await state.get_data()
    ism = data.get('ism')
    ha = data.get('ha')
    await message.answer(f"Sizning malumotlaringiz tasdiqlaysizmi\nIsm: {ism}\nQiziqish: {ha}\nDasturlash tili: {language}", reply_markup=menyu)
    await state.set_state(Hobby.view)
    
@dp.message(F.text)
async def ViewBot(message: Message, state: FSMContext):
    xabar = message.text
    if xabar == 'No':
        await message.answer("Siz boshqatdan ro'yhatdan o'ting")
        await state.clear()
    else:
        data = await state.get_data()
        ism = data.get('ism')
        ha = data.get('ha')
        language = data.get('language')
        await bot.send_message(chat_id=kanal_id, text=f"Bizga kelgan malumotlar\nIsm: {ism}\nQiziqish: {ha}\nDasturlash tili: {language}")
        await message.answer("kanalga yuborildi")
        await state.clear()

    
async def main():
    await bot.send_message(chat_id=7072212883, text="Bot ishga tushdi")
    await dp.start_polling(bot)
    
    
if  __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("tugadi")
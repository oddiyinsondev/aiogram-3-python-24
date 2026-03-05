import asyncio
from email import message
import logging
import token
import datetime
from aiogram import Bot, Dispatcher,F
from aiogram.types import Message
from aiogram.filters import CommandStart
from telegram_ai import t, adduser1,saqlash,cantact,menyu,mahsulot
import wikipedia
import json
wikipedia.set_lang('uz')

qidruv = []

bot = Bot(token=t)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(F.contact)
async def contact_handler(message: Message):
     if message.contact and message.contact.phone_number:
          telefon = message.contact.phone_number
     else: 
          telefon = None

     foydalanuvchi_id = message.from_user.id
     toliq_ismi = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
     foydalanuvchi_nomi = message.from_user.first_name
     adduser1(foydalanuvchi_nomi=foydalanuvchi_nomi, telegram_id=foydalanuvchi_id, toliq_ismi=toliq_ismi, telefon_raqami=telefon)

     await message.answer("Rahmat, kontakt qabul qilindi.")
     await message.answer("assalomu alaykum, sizni botimizga xush kelibsiz. Siz menyuni tanlab mahsulotlarimizni ko'rishingiz mumkin", reply_markup=menyu)
    
@dp.message(CommandStart())
async def start_handler(message: Message):
    foydalanuvchi_id = message.from_user.id
    toliq_ismi = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
    foydalanuvchi_nomi = message.from_user.first_name
    telefon = message.contact.phone_number if message.contact and message.contact.phone_number else None
    adduser1(foydalanuvchi_nomi=foydalanuvchi_nomi, telegram_id=foydalanuvchi_id, toliq_ismi=toliq_ismi, telefon_raqami=telefon)
    await message.answer("Assalomu alaykum 👋 Iltimos kontaktni yuboring.", reply_markup=cantact)


@dp.message(F.text == "qidruv")
async def qirivu(message:Message):
     qidruv.append(message.from_user.id)
     await message.answer("Nimani qidirmoqchisiz?")

@dp.message(F.text)
async def mbot(message: Message):
     text = message.text
     user = message.from_user.id
     if user in qidruv:
         try:
              wi = wikipedia.summary(text)
              await message.answer(f"siz qidirgan malumot\n\n {wi}")    
         except:     
                        await message.answer('xato malumot siz xato malumot kiritngiz')
     saqlash(message.from_user.id, text, None)
     if text == "⬅️ Orqaga":
          await message.answer("asosiy menyu", reply_markup=menyu)
     with open('mahsulot.json', 'r', encoding='utf-8') as f:
         mahsulotlar = json.load(f)
     if text ==  "Menyu 🍕":
          await message.answer("mahusulotlar ro'yxati", reply_markup=mahsulot(mahsulotlar))
     for i in mahsulotlar:
          if i['nomi'].lower()==text.lower():
               await message.answer(f"{i['nomi']}\nnarxi: {i['narxi']}")
               return
     saqlash(message.from_user.id, text)                
     
     
async def main():
    await bot.send_message(chat_id=6611222144, text="Bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



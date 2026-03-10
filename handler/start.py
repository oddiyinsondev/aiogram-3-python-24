from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from buttons.inlinebuttons.main import menu
from buttons.inlinebuttons.obuna import obuna_buttons
from aiogram.fsm.context import FSMContext
from states.tarjima import TranslateState
from config.config import kanal_id
from aiogram import Bot

start_router = Router()



@start_router.message(CommandStart())
async def StartBot(message: Message, bot:Bot):
    ism = message.from_user.first_name
    user_status = await bot.get_chat_member(kanal_id, message.from_user.id)
    if user_status.status == "left":
        await message.answer("Kanalga obuna bo'ling", reply_markup=obuna_buttons)
    else:
        await message.answer("Asslaomu alaykum foydalanishingiz mumkin", reply_markup=menu)

@start_router.callback_query(F.data=="tek")
async def TekBot(call: CallbackQuery,bot:Bot):
    user_id = call.from_user.id
    user_status = await bot.get_chat_member(kanal_id, user_id)
    if user_status.status == "left":
        await call.message.answer("Kanalga obuna bo'ling", reply_markup=obuna_buttons)
        await call.message.delete()
    else:
        await call.message.answer("Botdan foydalanishingiz mumkin", reply_markup=menu)
        await call.message.delete()
        




@start_router.callback_query(F.data == "tarjima")
async def TarjimaBot(call: CallbackQuery, state: FSMContext):
    await call.answer("Tarjima qilmoqchi soz kiriting")
    await state.set_state(TranslateState.tarjima)
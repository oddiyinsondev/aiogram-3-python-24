from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from buttons.inlinebuttons.main import menu
from aiogram.fsm.context import FSMContext
from states.tarjima import TranslateState

start_router = Router()

@start_router.message(CommandStart())
async def StartBot(message: Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu alaykum botga xush kelibsiz\n{ism}", reply_markup=menu)


@start_router.callback_query(F.data == "tarjima")
async def TarjimaBot(call: CallbackQuery, state: FSMContext):
    await call.answer("Tarjima qilmoqchi soz kiriting")
    await state.set_state(TranslateState.tarjima)
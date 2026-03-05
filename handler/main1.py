from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from translate import Translator
from gtts import gTTS
from states.tarjima import TranslateState
from buttons.inlinebuttons.main import menu
from aiogram.fsm.context import FSMContext

translate_router = Router()


@translate_router.message(F.text, TranslateState.tarjima)
async def TranslateBot(message: Message, state:FSMContext):
    xabar = message.text
    if xabar == 'yoq':
        await message.answer("siz asosiy sahifadasiz", reply_markup=menu)
        await state.clear()
    else:
        translator = Translator(from_lang='uz', to_lang="ru")
        translation = translator.translate(f"{xabar}")
        voice = gTTS(text=translation, lang='ru')
        voice.save('voice.mp3')
        musika = FSInputFile('voice.mp3')
        await message.answer_voice(voice=musika, caption=f"Tarjima text\n\n{translation}")


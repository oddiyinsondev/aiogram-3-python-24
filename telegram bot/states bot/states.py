from aiogram.fsm.state import State, StatesGroup


class Hobby(StatesGroup):
    name = State()
    hobby = State()
    language = State()
    view = State()
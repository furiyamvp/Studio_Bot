from aiogram.dispatcher.filters.state import StatesGroup, State


class AddPubgAccountState(StatesGroup):
    email = State()
    password = State()
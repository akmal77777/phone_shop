from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    full_name = State()
    phone_number = State()
    gender = State()
    location = State()
    exact_location = State()


class ProfileUpdate(StatesGroup):
    full_name = State()
    phone_number = State()
    gender = State()
    location = State()
    exact_location = State()

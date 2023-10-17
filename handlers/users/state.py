from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterState(StatesGroup):
    full_name = State()
    phone_number = State()
    gender = State()
    location = State()
    exact_location = State()



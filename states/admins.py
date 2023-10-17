from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductState(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()
    quantity = State()


class ProductUpdateState(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()
    quantity = State()
    delete = State()

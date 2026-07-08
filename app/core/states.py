from aiogram.fsm.state import StatesGroup, State

class OrderService(StatesGroup):
    enter_description = State()
    enter_adress = State()
    enter_name = State()
    enter_phone = State()
from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core import OrderService, push_order_to
from keyboards import cancel_kb, menu_kb

fsm_router = Router()

@fsm_router.message(F.text == "❌ Cancel order")
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state is None:
        return

    await state.clear()
  
    await message.answer(
        text="The order has been cancelled. You can select another service anytime.",
        reply_markup=menu_kb
    )

@fsm_router.message(OrderService.enter_description)
async def description_process(message: Message, state: FSMContext):
    await state.update_data(description=message.text)

    await state.set_state(OrderService.enter_name)
    await message.answer(text="Great! Now, please enter your name:", reply_markup=cancel_kb)


@fsm_router.message(OrderService.enter_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(OrderService.enter_adress)
    await message.answer(text="Got it. Please enter the service address:", reply_markup=cancel_kb)


@fsm_router.message(OrderService.enter_adress)
async def process_adress(message: Message, state: FSMContext):
    await state.update_data(adress=message.text)

    await state.set_state(OrderService.enter_phone)
    await message.answer(text="And finally, provide your phone number please:", reply_markup=cancel_kb)


@fsm_router.message(OrderService.enter_phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)

    user_data = await state.get_data()

    await push_order_to(
        user_id=message.from_user.id,
        username=message.from_user.username,
        order_data=user_data
    )

    await message.answer(
        text=f"Thank you, {user_data['name']}! Your request for '{user_data.get('service', 'service')}' has been received. "
             f"Our operator will contact you at {user_data['phone']} shortly.",
        reply_markup=menu_kb
    )

    await state.clear()
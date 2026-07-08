from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from core import OrderService
from loaders.pricelist_loader import PRICE_PAGES
from keyboards import get_price_keyboard, cancel_kb

callback_router = Router()

MIN_PRICES = {
    "furniture": 500,
    "appliances": 250,
    "complaint": 50,
    "measurement": 100,
    "electrical": 200
}

@callback_router.callback_query(F.data.in_(MIN_PRICES.keys()))
async def start_order_fsm(callback, state):
    service_key = callback.data
    min_price = MIN_PRICES[service_key]

    await state.update_data(
        service=service_key,
        base_price=min_price
    )

    await state.set_state(OrderService.enter_description)
    
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(
        text=f"Please provide more details about your order. "
             f"The price for this service starts at ${min_price}.\n\n",
             reply_markup=cancel_kb
    )
    await callback.answer()

@callback_router.callback_query(F.data.startswith("price_page"))
async def pagination(callback):
    page_index = int(callback.data.split(":")[1])
    target_page = PRICE_PAGES[page_index]
    kb = get_price_keyboard(page_index=page_index, total_pages=len(PRICE_PAGES))

    await callback.message.edit_text(
        text=target_page["text"],
        reply_markup=kb,
        parse_mode="Markdown"
    )

    await callback.answer()

@callback_router.callback_query(F.data == "ignore")
async def ignore_click(callback: CallbackQuery):
    await callback.answer()
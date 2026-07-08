import random

from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove

from filters.intent_filter import IntentFilter
from loaders.pricelist_loader import PRICE_PAGES
from keyboards.inline import get_price_keyboard
from keyboards import KEYBOARDS_MAP
from core import send_order_status

text_router = Router()
text_router.message.filter(F.chat.type == 'private')

@text_router.message(IntentFilter())
async def main_intent(message, intent_name, responses = None, action = None, next_state =  None, keyboard_name= None):

    reply_markup = KEYBOARDS_MAP.get(keyboard_name) or ReplyKeyboardRemove()
    select_response = random.choice(responses) if responses else "Request in progress..."

    if intent_name == "price_list":
        if not PRICE_PAGES:
            await message.answer("Sorry, price list is temporarily unavailable.")
        else:
            first_page = PRICE_PAGES[0]
            kb = get_price_keyboard(page_index=0, total_pages=len(PRICE_PAGES))
            await message.answer(
                text=first_page["text"],
                reply_markup=kb,
                parse_mode="Markdown"
            )
        return
    
    if action == "get_order_status":
        await send_order_status(message)
        return

    if next_state:
        await message.answer("Function on development staus...")
    else:
        await message.answer(text=select_response, reply_markup=reply_markup)
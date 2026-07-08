from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.inline import order_select_kb

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Order the service")
        ],
        [
            KeyboardButton(text="Price list"),
            KeyboardButton(text="Rewiews")
        ],
        [
            KeyboardButton(text="My order status")
        ]
    ],
    resize_keyboard=True
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❌ Cancel order")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


KEYBOARDS_MAP = {
    "menu_kb": menu_kb,
    "order_select_kb": order_select_kb
}
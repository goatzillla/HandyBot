from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

order_select_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Furniture assembly 🛋️', callback_data="furniture")],
        [InlineKeyboardButton(text='Connecting household appliances 📺', callback_data="appliances")],
        [InlineKeyboardButton(text='Furniture complaint 🛠️', callback_data="complaint")],
        [InlineKeyboardButton(text='Measurement 📐', callback_data="measurement")],
        [InlineKeyboardButton(text='Electrical repair or installation 🔌', callback_data="electrical")]
    ]
)


def get_price_keyboard(page_index: int, total_pages: int) -> InlineKeyboardMarkup:
    buttons = []
    
    if page_index > 0:
        buttons.append(InlineKeyboardButton(text="◀️ Back", callback_data=f"price_page:{page_index - 1}"))
        
    buttons.append(InlineKeyboardButton(text=f"{page_index + 1} / {total_pages}", callback_data="ignore"))
    
    if page_index < total_pages - 1:
        buttons.append(InlineKeyboardButton(text="Next ▶️", callback_data=f"price_page:{page_index + 1}"))

    return InlineKeyboardMarkup(inline_keyboard=[buttons])
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards.reply import menu_kb

cmd_router = Router()

@cmd_router.message(CommandStart())
async def start_cmd(message):
    await message.answer(text="Welcome to our handyman service 🔨. Here, you can submit a request for the installation, connection, or assembly of appliances📺, electronics🔌 , and furniture🛋️. We, in turn, will strive to provide you with the fastest and highest-quality service.", reply_markup = menu_kb)
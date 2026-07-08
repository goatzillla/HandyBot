from aiogram.types import Message

from core.db_service import get_orders_by_user
from keyboards import menu_kb

STATUS_LABELS = {
    "pending": "🕓 Pending",
    "in_progress": "🔧 In progress",
    "done": "✅ Done",
    "cancelled": "❌ Cancelled",
}


async def send_order_status(message: Message):
    orders = await get_orders_by_user(message.from_user.id)

    if not orders:
        await message.answer(
            text="You don't have any orders yet. Tap \"Order the service\" to create one.",
            reply_markup=menu_kb
        )
        return

    blocks = []
    for order in orders:
        status_label = STATUS_LABELS.get(order["status"], order["status"])
        blocks.append(
            f"🧾 Order #{order['order_id']}\n"
            f"Service: {order.get('service') or '—'}\n"
            f"Status: {status_label}\n"
            f"Created: {order['created_at']}"
        )

    text = "Your recent orders:\n\n" + "\n\n".join(blocks)
    await message.answer(text=text, reply_markup=menu_kb)
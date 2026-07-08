import asyncio
import os
import logging

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("bot.log", encoding="utf-8"),
    ],
)

logger = logging.getLogger(__name__)

from handlers import cmd_router, text_router, callback_router, fsm_router
from loaders.knowledge_loader import load_knowledge_base
from core.db_service import init_db

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

redis_client = Redis(host=REDIS_HOST, port=6379, decode_responses=True)
storage = RedisStorage(redis_client)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_routers(cmd_router, callback_router, fsm_router, text_router)

async def main():
    load_knowledge_base()
    await init_db()
    logger.info("Bot started successfully")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
import os
import aiosqlite
import logging 

logger = logging.getLogger(__name__)

from datetime import datetime


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
DB_PATH = os.path.join(BASE_DIR, "database", "orders.db")

async def init_db():

    folder_path = os.path.dirname(DB_PATH)
    os.makedirs(folder_path, exist_ok=True)
    
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
            order_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            username    TEXT,
            service     TEXT,
            base_price  REAL,
            client_name TEXT,
            phone       TEXT,
            address      TEXT,
            description TEXT,
            status      TEXT NOT NULL DEFAULT 'pending',
            created_at   TEXT NOT NULL
            )
            """
        )
        await db.execute("CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id)")
        await db.commit()
    logger.info("SQLite database initialized successfully")


async def push_order_to(user_id, username, order_data):
    try:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username_str = f"{username}" if username else "No username"

        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                """
                INSERT INTO orders (
                    user_id, username, service, base_price,
                    client_name, phone, address, description,
                    status, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    username_str,
                    order_data.get("service"),
                    order_data.get("base_price"),
                    order_data.get("name"),
                    order_data.get("phone"),
                    order_data.get("adress") or order_data.get("address"),
                    order_data.get("description"),
                    "pending",
                    created_at,
                ),
            )
            await db.commit()
            order_id = cursor.lastrowid

        logger.info(f"Order #{order_id} from {username_str} (user_id={user_id}) saved successfully")
        return order_id
    
    except Exception as e:
        logger.exception(f"Failed to save order for user_id={user_id}: {e}")
        return None
    
async def get_orders_by_user(user_id, limit=5):
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT order_id, service, base_price, client_name, phone, address, description, status, created_at
                FROM orders
                WHERE user_id = ?
                ORDER BY order_id DESC
                LIMIT ?
                """,
                (user_id, limit)
            )
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
        
    except Exception as e:
        logger.exception(f"Failed to fetch orders for user_id={user_id}: {e}")
        return []
    
async def update_order_status(order_id, status):
    #UPDATE for admin panels
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "UPDATE orders SET status = ? WHERE order_id = ?",
                (status, order_id),
            )
            await db.commit()
        logger.info(f"Order #{order_id} status updated to '{status}'")
        return True
    
    except Exception as e:
        logger.exception(f"Failed to update status for order #{order_id}: {e}")
        return False
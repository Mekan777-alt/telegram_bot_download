from config import db, dp, bot
import logging
from handlers import start, profile, help
import asyncio


async def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger(__name__)
    db.create_tables()
    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(help.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

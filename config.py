import asyncio
from aiogram import Bot, Dispatcher
import os
from aiogram.fsm.storage.memory import MemoryStorage
from data.db import Database
from dotenv import load_dotenv

load_dotenv()

storage = MemoryStorage()
loop = asyncio.get_event_loop()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage, loop=loop)

path = os.getcwd() + "/database.sqlite"
db = Database(path)

from config import Config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


# initial telegram bot parameters
telegram_bot = Bot(token=Config.BOT_TOKEN)
storage = MemoryStorage()
telegram_dispatcher = Dispatcher(storage=storage)

# telegram bot init function
async def initialize_telegram_bot():
    await telegram_bot.delete_webhook(drop_pending_updates=True)
from aiogram import Router, Bot
from .handlers import setup_handlers


def init_task_router(bot: Bot) -> Router:
    router = Router()
    setup_handlers(router, bot)
    return router
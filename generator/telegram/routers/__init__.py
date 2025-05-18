from aiogram import Router, Dispatcher, Bot
from .CommonRouter import init_common_router


def init_routers(dispatcher: Dispatcher, bot: Bot) -> None:
    # initialize the common router
    dispatcher.include_router(init_common_router(bot))
from aiogram import Router, Dispatcher, Bot
from .CommonRouter import init_common_router
from .TaskRouter import init_task_router

import logging


logger = logging.getLogger(__name__)

def init_routers(dispatcher: Dispatcher, bot: Bot) -> None:
    # initialize the common router
    dispatcher.include_router(init_common_router(bot))
    logger.debug('Common router initialized')

    # initialize the task router
    dispatcher.include_router(init_task_router(bot))
    logger.debug('Task router initialized')
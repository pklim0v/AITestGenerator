from dotenv import load_dotenv
load_dotenv()

import logging
from config import Config

import asyncio

# telegram imports
from generator.telegram import telegram_bot, telegram_dispatcher, initialize_telegram_bot

def logging_setup():
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    if Config.LOG_LEVEL == "DEBUG":
        logging.basicConfig(level=logging.DEBUG, format=log_format)

    else:
        logging.basicConfig(level=logging.INFO, format=log_format)


async def main():
    await initialize_telegram_bot()
    await telegram_dispatcher.start_polling(telegram_bot)

if __name__ == '__main__':

    # logging setup
    logging_setup()

    # run bot
    asyncio.run(main())

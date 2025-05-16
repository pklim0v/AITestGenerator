import os


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    AI_TYPES = [
        'claude'
    ]
    QUESTIONS_COUNT = 5
    ANSWERS_COUNT = 4
    LANGUAGE = 'Russian'
    TOPICS = [
        BASE_DIR + '/sources/1.pdf'
    ]
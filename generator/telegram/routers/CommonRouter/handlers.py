from aiogram import types, Router, Bot
from aiogram.filters import Command
from generator.tester import generate_task
from config import Config
from generator.telegram import keyboards


def setup_handlers(router: Router, bot: Bot) -> None:
    @router.message(Command(commands=["start"]))
    async def start_command(message: types.Message):
        # task = await generate_task(0, Config.AI_TYPES[0], Config.QUESTIONS_COUNT, Config.ANSWERS_COUNT, Config.LANGUAGE)
        await message.answer(text="Hi there! I can generate questions for you. Press the button:",
                             reply_markup=keyboards.get_intro_keyboard(),
                             parse_mode='Markdown')
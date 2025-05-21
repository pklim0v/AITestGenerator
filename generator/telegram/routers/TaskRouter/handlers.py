from aiogram import types, Router, Bot
from aiogram.filters import Command
from generator.tester import generate_task
from generator.telegram import keyboards, texts
from config import Config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import random
import logging

from generator.tester import Question, Task


logger = logging.getLogger(__name__)


class TaskStates(StatesGroup):
    asking_questions =State()
    # checking_results = State()


def setup_handlers(router: Router, bot: Bot) -> None:
    @router.callback_query(lambda c: c.data == "generate_task")
    async def task_generation_request(callback_query: types.CallbackQuery, state: FSMContext) -> None:
        try:
            await bot.answer_callback_query(callback_query.id)
            message = await bot.send_message(callback_query.from_user.id, text="Generating task, please wait...")
            task = await generate_task(0, Config.AI_TYPES[0], Config.QUESTIONS_COUNT, Config.ANSWERS_COUNT, Config.LANGUAGE)
            await bot.delete_message(callback_query.from_user.id, message.message_id)
            await bot.send_message(callback_query.from_user.id, text="Task generated successfully!")

        except Exception as e:
            logger.error(f'Error occurred while generating task: {e}')

        # uploading generated task to state
        await state.update_data(task=task,
                                question_number=0)

        # await bot.send_message(callback_query.from_user.id,
        #                        text=texts.generate_question_text(task.questions[0].question),
        #                        reply_markup=keyboards.get_task_keyboard(task.questions[0].answers),
        #                        parse_mode='Markdown')
        await state.set_state(TaskStates.asking_questions)
        await send_question(callback_query, state)



    async def send_question(callback_query: types.CallbackQuery, state: FSMContext) -> None:
        data = await state.get_data()
        task = data.get('task')
        question_number = data.get('question_number')

        if question_number >= len(task.questions):
            await state.set_state()
            await bot.send_message(callback_query.from_user.id,
                                   text=texts.generate_task_result_text(task),
                                   reply_markup=keyboards.get_intro_keyboard(),
                                   parse_mode='MarkdownV2')


        else:
            # random the answers order
            answers_order = list(range(len(task.questions[question_number].answers)))
            random.shuffle(answers_order)

            # send the question to the current user
            message = await bot.send_message(callback_query.from_user.id,
                                   text=texts.generate_question_text(task.questions[question_number],
                                                                     answers_order),
                                   reply_markup=keyboards.get_task_keyboard(answers_order),
                                   parse_mode='MarkdownV2')

            # saving message.id
            await state.update_data(last_message_id=message.message_id)


    # proceesing the given answer
    @router.callback_query(lambda c: c.data.startswith("answer_"), TaskStates.asking_questions)
    async def answer_processing(callback_query: types.CallbackQuery, state: FSMContext) -> None:
        try:
            await bot.answer_callback_query(callback_query.id)
            data = await state.get_data()
            task = data.get('task')
            question_number = data.get('question_number')
            last_message_id = data.get('last_message_id')
            answer_number = int(callback_query.data.split('_')[1])
            await bot.delete_message(callback_query.from_user.id, last_message_id)

        except Exception as e:
            logger.error(f'Error occurred while processing answer: {e}')

        try:
            # question = task.questions[question_number]
            # question.check_answer(answer_number)
            # pass
            task.questions[question_number].check_answer(answer_number)
            pass

        except Exception as e:
            logger.error(f'Error occurred while checking answer: {e}')

        question_number += 1

        await state.update_data(task=task,
                                question_number=question_number)

        await send_question(callback_query, state)




    # @router.callback_query(lambda c: c.data.startswith("topic_"))

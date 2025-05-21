import aiogram.utils.markdown as md
from generator.tester import Question, Task
import random


def generate_question_text(question: Question, answers: list) -> str:

    text = md.text(md.bold('Вопрос:'),
                   '\n\n',
                   md.code(question.question),
                   '\n\n',
                   md.bold('Выберете вариант ответа:'), '\n\n')

    for i in range(len(answers)):
        text += md.text(md.bold(f'{i + 1}. '), md.code(question.answers[int(answers[i])]), '\n\n')

    text += '\n'

    return text

def generate_task_result_text(task: Task) -> str:
    # calculating result percentage
    correct_answers_count = 0
    for question in task.questions:
        if question.is_answered_correctly:
            correct_answers_count += 1

    correct_answers_percentage = round(correct_answers_count / len(task.questions) * 100, 2)

    # generating result text

    text = md.text(
        md.text('Задание завершено\!'),
        '\n\n',
        md.text(f'Процент правильных ответов: '),
        md.bold(f'{correct_answers_percentage}%'),
        '\n\n',
        md.text(f'Правильных ответов: {correct_answers_count} из {len(task.questions)}'),
        '\n\n',
        md.text('Ниже приведены вопросы и ответы:'),
        '\n\n'
    )

    for question in task.questions:
        if question.is_answered_correctly:
            text += md.text(
                md.bold('Вопрос: '),
                md.code(question.question),
                '\n\n',
                md.bold('Ваш ответ: '),
                md.code(question.answers[question.user_answer]),
                '   ',
                md.bold('(Правильный ответ)'),
                '\n\n\n\n'
            )
        else:
            text += md.text(
                md.bold('Вопрос: '),
                md.code(question.question),
                '\n\n',
                md.bold('Ваш ответ: '),
                md.code(question.answers[question.user_answer]),
                '\n\n',
                md.bold('Правильный ответ: '),
                md.code(question.answers[0]),
                '\n\n\n\n'
            )

    return text
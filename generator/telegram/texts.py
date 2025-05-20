import aiogram.utils.markdown as md
import random


def generate_question_text(question, answers):

    text = md.text(md.bold('Вопрос:'),
                   '\n\n',
                   md.code(question.question),
                   '\n\n',
                   md.bold('Выберете вариант ответа:'), '\n\n')

    for i in range(len(answers)):
        text += md.text(md.bold(f'{i + 1}. '), md.code(question.answers[int(answers[i])]), '\n')

    text += '\n'

    return text
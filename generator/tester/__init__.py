import logging
from config import Config
from generator.ai import generate_task_json
import re
import json

logger = logging.getLogger(__name__)

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
        self.is_answered_correctly = False
        self.user_answer = None


    def check_answer(self, answer):
        #answer validation
        if len(self.answers) == 0:
            raise ValueError('No answers provided')
        elif answer >= len(self.answers) or answer < 0:
            raise ValueError('Answer is not in the list of answers')

        if answer == 0:
            self.is_answered_correctly = True
            self.user_answer = answer
        else:
            self.is_answered_correctly = False
            self.user_answer = answer

    def __repr__(self):
        return f'Question: {self.question}\nAnswers: {self.answers}\nCorrect: {self.is_answered_correctly}'


class Task:
    def __init__(self, topic, questions):
        self.topic = topic
        self.questions = []
        for question in questions:
            new_question_obj = Question(question[0], question[1])
            self.questions.append(new_question_obj)

        self.incorrectly_answered_questions = []

    @classmethod
    async def generate_task(cls, topic, ai_type, question_count, answers_count, language):
        response_json = await generate_task_json(topic, ai_type, question_count, answers_count, language)
        if response_json is None:
            raise ValueError('Error occurred while generating task. Response JSON is None')
        else:
            logger.debug(f'Task generated successfully: {response_json}')
            questions = cls._extract_questions_from_response(response_json)
            return cls(topic, questions)

    @staticmethod
    def _extract_questions_from_response(response_json):

        json_match = re.search(r'```json\s*(.*?)\s*```', response_json, re.DOTALL)
        if json_match:
            content = json_match.group(1)
            logger.debug(content)

        parsed_questions = []
        questions = json.loads(content)

        for question in questions:
            parsed_question = [question['question']]
            parsed_answers = []
            for answer in question['options']:
                parsed_answers.append(answer['text'])
            parsed_question.append(parsed_answers)
            parsed_questions.append(parsed_question)

        return parsed_questions



async def generate_task(topic, ai_type, question_count, answers_count, language):
    try:
        task = await Task.generate_task(topic, ai_type, question_count, answers_count, language)
        return task

    except Exception as e:
        logger.error(f'Error occurred while generating task: {e}')
        return None


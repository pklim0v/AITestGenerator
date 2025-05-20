import generator.ai.claude as claude
from config import Config

import logging

logger = logging.getLogger(__name__)


# def get_ai_client(ai_type: str):
#     if ai_type == 'claude':
#         return claude
#     else:
#         raise ValueError(f'AI type {ai_type} is not supported for now')
#
#
# async def generate_question(ai_client, topic, questions_count, answers_count):
#     client = get_ai_client(ai_client)

# async def generate_task(ai_client, topic):
#     if ai_client == 'claude':
#         try:
#             file_id = await claude.upload_file(Config.TOPICS[topic])
#
#         except Exception as e:
#             logger.error(f'Error occurred while uploading file: {e}')
#             return None
#
#     logger.debug(f'File {Config.TOPICS[topic]} uploaded to Claude. File ID: {file_id}')
#     return file_id

async def generate_task_json(topic, ai_type, question_count, answers_count, language):
    if ai_type == 'claude':
        try:
            response_json = await claude.generate_json(Config.TOPICS[topic], question_count, answers_count, language)
            return response_json

        except Exception as e:
            logger.error(f'Error occurred while generating task: {e}')
            return None

    else:
        raise ValueError(f'AI type {ai_type} is not supported for now')




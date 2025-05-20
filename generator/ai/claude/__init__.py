import anthropic
from config import Config
import os
import json
import base64

from .prompts import get_prompt

client = anthropic.Anthropic(api_key=Config.CLAUDE_API_KEY)

# async def upload_file(file_path: str):
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f'File {file_path} does not exist')
#
#     with open(file_path, 'rb') as file:
#         file_content = file.read()
#
#     pdf_data = base64.b64encode(file_content).decode('utf-8')
#
#     response = client.messages.create(
#         model='claude-3-7-sonnet-20250219',
#         max_tokens=1000,
#         messages=[
#             {"role": "user",
#              "content": [
#                  {
#                      "type": "document",
#                      "source": {
#                          "type": "base64",
#                          "media_type": "application/pdf",
#                          "data": pdf_data
#                      }
#                  },
#                  {
#                      "type": "text",
#                      "text": "Confirm successful upload of the file"
#                  }
#         ]
#              }
#         ]
#     )
#
#     return response

async def generate_json(file_path, question_count, answers_count, language):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File {file_path} does not exist')

    with open(file_path, 'rb') as file:
        file_content = file.read()

    pdf_data = base64.b64encode(file_content).decode('utf-8')

    prompt = get_prompt(question_count, answers_count, language)

    response = client.messages.create(
        model='claude-3-7-sonnet-20250219',
        max_tokens=4000,
        messages=[
            {"role": "user",
             "content": [
                 {
                     "type": "document",
                     "source": {
                         "type": "base64",
                         "media_type": "application/pdf",
                         "data": pdf_data
                     }
                 },
                 {
                     "type": "text",
                     "text": prompt
                 }
             ]
             }
        ]
    )

    return response.content[0].text

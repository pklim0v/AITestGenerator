def get_prompt(questions_count, answers_count, language):
    prompt = (f'Based on the attached file, create {questions_count} questions and {answers_count} answer options for each question, where only '
              f'one answer is correct. Both questions and answers should be in {language} language. The correct answer '
              f'should always be the first option in the list of answers. '
              f'Provide the result in the following JSON format: ')


    prompt +='''
    [
          {
            "question": "Question's text",
            "options": [
              {"text": "First Answer's text"},
              {"text": "Second Answer's text"},
              ...
            ],
          },
          ...
        ]
    '''
    return prompt
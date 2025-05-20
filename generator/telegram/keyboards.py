from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

def get_intro_keyboard():
    button = InlineKeyboardButton(text="Generate task", callback_data="generate_task")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard

def get_task_keyboard(answers):

    buttons = []

    # create buttons for each answer, button num is in a row, callback data is answers order in question's answers list
    for i in range(len(answers)):
        button = InlineKeyboardButton(text=f'{i+1}', callback_data=f"answer_{answers[i]}")
        buttons.append(button)

    # create a keyboard with 2 buttons in each row
    ordered_buttons = []
    for i in range(0, len(buttons), 2):
        ordered_buttons.append(buttons[i:i+2])


    keyboard = InlineKeyboardMarkup(inline_keyboard=ordered_buttons)

    return keyboard

def get_topic_selection_keyboard():

    button = InlineKeyboardButton(text='Тема 1', callback_data='topic_1')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

    return keyboard

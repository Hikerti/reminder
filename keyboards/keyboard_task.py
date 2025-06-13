from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def keyboard_function_task(task_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Изменить название', callback_data=f'update_title_task:{task_id}'), InlineKeyboardButton(text='Изменить описание', callback_data=f'update_description_task:{task_id}')],
            [InlineKeyboardButton(text='Удалить задачу', callback_data=f'delete_task:{task_id}')],
        ])

keyboard_finily_create_task = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отправить', callback_data='send_task')],
        [InlineKeyboardButton(text='Отменить', callback_data='delete_task')]
    ])
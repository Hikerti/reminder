from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboards_create_task = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отправить', callback_data='send_task')],
    ]) 

keyboard_function_task = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Изменить название', callback_data='delete_task'), InlineKeyboardButton(text='Изменить описание', callback_data='delete_task')],
        [InlineKeyboardButton(text='Удалить задачу', callback_data='send_task')],
    ])

keyboard_finily_create_task = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отправить', callback_data='send_task')],
        [InlineKeyboardButton(text='Отменить', callback_data='delete_task')]
    ])
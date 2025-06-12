from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboards_user_create = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отменить регистрацию', callback_data='cancel_registration')]
    ])

keyboards_user_finily = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отправить данные', callback_data='confirm_registration')],
        [InlineKeyboardButton(text='Отменить регистрацию', callback_data='cancel_registration')]
    ])

keyboards_cancel_session = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Да, уверен', callback_data='cancel_session')],
        [InlineKeyboardButton(text='Нет, я остаюсь', callback_data='no_cancel_session')]
    ])
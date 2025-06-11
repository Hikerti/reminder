from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def start_user_no_registration(message: Message):
    await message.answer('Привет, друг!\n\n'
                         'Тебя приветствует Reminder бот, я умею составлять запоминалки. Зарегистрируйся и мы начнём.\n\n'
                         'Команда для регестрации /registration');

@router.message(Command(commands='cancel'))
async def cancel_user_no_registration(message: Message):
    keybords = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Да, уверен', callback_data='cancel_session')],
        [InlineKeyboardButton(text='Нет, я остаюсь', callback_data='no_cancel_session')]
    ])

    await message.answer('Вы точно хотите выйти из бота?', reply_markup=keybords);

@router.callback_query(lambda c: c.data in ['cancel_session', 'no_cancel_session'])
async def callback_cancel_session(callback: CallbackQuery):
    if callback.data == 'cancel_session':
        await callback.message.edit_text('Сессия успешно завершена');
    else: await callback.message.edit_text('Сессия успешно продолжена, приятного пользования');
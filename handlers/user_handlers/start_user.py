from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '...')))

from keyboards.keyboard_user import keyboards_cancel_session
from model.model_db import delete_user

router = Router()

@router.message(CommandStart())
async def start_user_no_registration(message: Message):
    await message.answer('Привет, друг!\n\n'
                         'Тебя приветствует Reminder бот, я умею создовать заметки. Зарегистрируйся и мы начнём.\n\n'
                         'Команда для регистрации /registration');

@router.message(Command(commands='exit'))
async def cancel_user_no_registration(message: Message):
    await message.answer('Вы точно хотите выйти из бота?', reply_markup=keyboards_cancel_session);

@router.callback_query(lambda c: c.data in ['cancel_session', 'no_cancel_session'])
async def callback_cancel_session(callback: CallbackQuery):
    if callback.data == 'cancel_session':
        user = delete_user(int(callback.from_user.id))
        if user: 
            await callback.message.edit_text('Сессия успешно завершена');
        else: await callback.message.edit_text('Вы не зарегистрированны ');
    else: await callback.message.edit_text('Сессия успешно продолжена, приятного пользования');
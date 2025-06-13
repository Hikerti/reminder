from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '...')))

from model.model_db import get_user

router = Router()

@router.message(Command(commands='view_user'))
async def process_view_user(message: Message):
    data = get_user(int(message.from_user.id))

    if data: 
        text = (
            f"Твой данные:\n\n"
            f"👤 Имя: {data.name_user}\n"
            f"👥 Фамилия: {data.surname_user}\n"
            f"🎂 Возраст: {data.age_user}\n"
            f"🔐 Логин: {data.login_user}\n"
            f"🛡️ Пароль: {'*' * len(data.password_user)}"
        )

        await message.answer(text)
    else: await message.answer('Ты ещё не зарегистрировался.\n\n' 
                               'Введи /registration, чтобы зарегистрироваться')    
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '...')))

from model.model_db import view_tasks
from keyboards.keyboard_task import keyboard_function_task

router = Router()

@router.message(Command(commands='view_tasks'))
async def process_view_tasks_list(message: Message):
    user_id = message.from_user.id
    tasks = view_tasks(user_id)

    if not tasks: 
        await message.answer('У вас пока нет задач\n\n'
                             'Создайте заметку при помощи комманды /create_task')
        return
    await message.answer('Ваши задачи:')

    for task in tasks:
        text = f"📌 <b>{task.title}</b>\n\n{task.description}"
        await message.answer(text, parse_mode="HTML", reply_markup=keyboard_function_task(task.id))
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '...')))

from model.model_db import delete_tasks

router = Router()

@router.callback_query(lambda c: c.data.startswith('delete_task:'))
async def process_delete_task(callback: CallbackQuery):
    task_id_string = callback.data.split(':')[1]
    task_id = int(task_id_string)

    success = delete_tasks(task_id)
    if success: 
        await callback.message.edit_text('Задача успешно удалена')
    else:
        await callback.message.edit_text('Задача успешно удалена')   
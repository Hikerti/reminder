from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '...')))

from model.model_db import create_task_from_dict
from keyboards.keyboard_task import keyboard_finily_create_task, keyboards_create_task

router = Router()
class CreateTask(StatesGroup):
    title = State()
    description = State()

@router.message(Command(commands='create'))
async def process_create_task(message: Message, state: FSMContext):
    await state.set_state(CreateTask.title)
    await message.answer('Введите заголовок для заметки', reply_markup=keyboards_create_task)

@router.message(CreateTask.title) 
async def process_add_title(message: Message, state: FSMContext):
    if (len(message.text) < 2):
        await message.answer('Заголовок заметки должен быть минимум 2 символов')

    await state.update_data(title=message.text)
    await state.set_state(CreateTask.description)
    await message.answer('Введите описание заметки', reply_markup=keyboards_create_task)

@router.message(CreateTask.description)
async def process_add_description(message: Message, state: FSMContext):
    if (len(message.text) < 10):
        await message.answer('Текст для заметки должен быть минимум 10 символов')
        return

    await state.update_data(description=message.text)

    await message.answer('Отлично! Подтвердите создание заметки', reply_markup=keyboard_finily_create_task)

@router.callback_query(lambda c: c.data in ['send_task', 'delete_task'])
async def process_send_task(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback.data == 'send_task':
        task_data = {
            "id_task": 1,
            "id_user": callback.from_user.id,
            "title": data.get("title"),
            "description": data.get("description")
        }

        create_task_from_dict(task_data)

        await callback.message.edit_text(f'Задача создана {task_data}')
    else: await callback.message.edit_text('Отправка задачи отменена')

    await state.clear()
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '...')))

from model.model_db import update_task_title

router = Router()

class UpdateTitleState(StatesGroup):
    wait_set_title = State()

@router.callback_query(lambda c: c.data.startswith('update_title_task:'))
async def process_update_task_title(callback: CallbackQuery, state: FSMContext):
    task_id_string = callback.data.split(':')[1]
    task_id = int(task_id_string)

    await state.update_data(task_id=task_id)
    await state.set_state(UpdateTitleState.wait_set_title)

    await callback.message.edit_text('Введите новый заголовок')
        
@router.message(StateFilter(UpdateTitleState.wait_set_title))
async def process_set_task_title(message: Message, state: FSMContext):
    data = await state.get_data()
    task_id = data['task_id']
    task_text = message.text

    success = update_task_title(task_id, task_text)

    if success: 
        await message.answer('Заголовок задачи успешно обнавлён.')
    else:
        await message.answer('Заголовок задачи не обнавлён.') 

    await state.clear()     
                   
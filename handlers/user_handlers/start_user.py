from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def start_user_no_registration(message: Message):
    await message.answer('Начало работы');

@router.message(Command(commands='cancel'))
async def cancel_user_no_registration(message: Message):
    await message.answer('Конец работы');
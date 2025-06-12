from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_command(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начало работы'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='registration', description='Регистрация пользователя'),
        BotCommand(command='createtask', description='Создать заметку'),
    ]
    await bot.set_my_commands(commands)
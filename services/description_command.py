from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_command(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начало работы'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='exit', description='Выход'),
        BotCommand(command='registration', description='Регистрация пользователя'),
        BotCommand(command='create_task', description='Создать заметку'),
        BotCommand(command='view_user', description='Данные пользователя'),
        BotCommand(command='view_tasks', description='Посмотреть заметки'),
    ]
    await bot.set_my_commands(commands)
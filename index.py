import asyncio
from aiogram import Bot, Dispatcher
from config.config import Config, load_config

from handlers.user_handlers import start_user, user_registration
from handlers.task_handlers import create_task, view_tasks_user

from services.description_command import set_bot_command

async def main() -> None:
    dp = Dispatcher()

    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)

    dp.include_router(start_user.router)
    dp.include_router(user_registration.router)
    dp.include_router(create_task.router)
    dp.include_router(view_tasks_user.router)
    
    await set_bot_command(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot);


asyncio.run(main())


import asyncio
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers.user_handlers import start_user, user_registration

async def main() -> None:
    dp = Dispatcher()

    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)

    dp.include_router(start_user.router)
    dp.include_router(user_registration.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot);

asyncio.run(main())
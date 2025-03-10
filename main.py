import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis 
from app.core.middlewares import Middleware
from database.models import async_main
from app.handlers import __all__ as all_routers
from app.core.utils.config import TOKEN



async def main():
    redis = Redis(host="localhost", port=6379, db=0)
    storage = RedisStorage(redis)
    
    await async_main()
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        request_timeout = 60
    )
    
    dp = Dispatcher(storage=storage)
    
    # Подключаем middleware
    dp.message.middleware(Middleware())
    dp.callback_query.middleware(Middleware())

    
    # Подключаем все роутеры
    dp.include_routers(*all_routers)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")
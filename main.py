from handlers.handlers import registration
import asyncio
from aiogram import Dispatcher, Bot


async def main():
    bot = Bot(token='TOKEN')
    dp = Dispatcher()
    registration(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

import asyncio
from aiogram import Dispatcher
from animals_defender import router
from bot_instance import bot  # Импортируем bot из bot_instance

dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

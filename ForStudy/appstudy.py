import asyncio  # импортируем библиотеку asyncio, для того чтобы использовать async, await
import os
from aiogram import Bot, Dispatcher, types  # импортируем библиотеку
# аиограмм, также из аиограмма
# берем бот, диспетчер и тайпс
from aiogram.filters import CommandStart  # Импортируем фильтры из аиограмма для нашей комманды старт
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv('TOKEN'))  # Токен для бота
dp = Dispatcher()  # вызываем диспетчер


async def main():  # Функция для запуска бота
    await bot.delete_webhook()
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())  # Активируем функцию запуска бота.

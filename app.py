import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from common import bot_cmds_list

from dotenv import find_dotenv, load_dotenv

from common.bot_cmds_list import private
from handlers.admin_private import admin_router
from handlers.user_group import user_group_router

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router

ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(admin_router)
dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook()
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())

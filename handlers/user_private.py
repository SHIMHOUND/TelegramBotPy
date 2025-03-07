from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())  # Простая функция использую команду старт,
# чтобы бот выдавал сообщение от сообщения /start
async def start(message: types.Message):
    await message.answer("Hi, Im virtual helper")


@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "menu")))
async def menu_cmd(message: types.Message):
    await message.answer("Here is menu: ")


@user_private_router.message(F.text.lower() == "about us")
@user_private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("About us: ")


@user_private_router.message(F.text.lower() == "payment methods")
@user_private_router.message(Command('payment'))
async def payment(message: types.Message):
    await message.answer("Payment methods: ")


@user_private_router.message(F.text, F.text.lower().contains('ship') | (F.text.lower() == 'shipping'))
@user_private_router.message(Command('shipping'))
async def shipping(message: types.Message):
    await message.answer("Shipping methods: ")




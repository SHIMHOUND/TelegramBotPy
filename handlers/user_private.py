from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.enums import parse_mode, ParseMode
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter

from kbds.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())  # Простая функция использую команду старт,
# чтобы бот выдавал сообщение от сообщения /start
async def start_cmd(message: types.Message):
    await message.answer(
        "Hi, I'm your virtual assistant",
        reply_markup=get_keyboard(
            'Menu',
            'About us',
            'Payment methods',
            'Shipping methods',
            'Send phone number',
            placeholder='What you want to know?',
            sizes=(2, 2)
        ),
    )


@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'menu')))
async def menu_cmd(message: types.Message):
    await message.answer("Here is menu: ")


@user_private_router.message(F.text.lower() == "about us")
@user_private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("About us: ")


@user_private_router.message(F.text.lower() == "payment methods")
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold("Payment methods:"),
        "By card in bot",
        "Upon receipt, card/cash",
        "In establishment",
        marker='✅ '
    )
    await message.answer(text.as_html())


@user_private_router.message(F.text, F.text.lower().contains('ship') | (F.text.lower() == 'shipping'))
@user_private_router.message(Command('shipping'))
async def shipping(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Shipping methods:"),
            'Curier',
            "By your self",
            "Get a table in establishment",
            marker='✅ '
        ),
        as_marked_section(
            Bold("Prohibited methods: "),
            "By mail",
            "By pigeons, what?",
            marker='❌ '
        ),
        sep="\n-----------------------\n"
    )
    await message.answer(text.as_html())


# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer(f"Contact received✅{get_contact}")
#     await message.answer(str(message.contact))
#
#
# @user_private_router.message(F.location)
# async def get_location(message: types.Message):
#     await message.answer(f"Location received✅{get_location}")
#     await message.answer(str(message.location))

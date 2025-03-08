from aiogram import F, Router, types
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds.reply import get_keyboard


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


ADMIN_KB = get_keyboard(
    'Add product',
    'Change product',
    'Delete product',
    'Just to look',
    placeholder="Choose action",
    sizes=(2, 2, 1),
)


@admin_router.message(Command('admin'))
async def add_product(message: types.Message):
    await message.answer('Ok, here is the list of products')


@admin_router.message(F.text == "Just to look")
async def starring_at_product(message: types.Message):
    await message.answer('Ok, here is the list of products')


@admin_router.message(F.text == "Change product")
async def change_product(message: types.Message):
    await message.answer('Ok, here is the list of products')


@admin_router.message(F.text == "Delete product")
async def delete_product(message: types.Message):
    await message.answer('Choose the product(s) to delete')



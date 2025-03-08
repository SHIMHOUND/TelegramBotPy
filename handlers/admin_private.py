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
    sizes=[2, 2, 1]
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


# Fsm state machine -->

@admin_router.message(F.text == 'Add product')
async def add_product(message: types.Message):
    await message.answer(
        'Enter the name of the product you want to add', reply_markup=types.ReplyKeyboardRemove()
    )


@admin_router.message(Command('Cancel'))
@admin_router.message(F.text.casefold() == 'cancel')
async def cancel_handler(message: types.Message) -> None:
    await message.answer('Actions cancelled', reply_markup=ADMIN_KB)


@admin_router.message(Command('Back'))
@admin_router.message(F.text.casefold() == 'back')
async def back_handler(message: types.Message) -> None:
    await message.answer(f'Ok, you are back to the previous step')


@admin_router.message(F.text)
async def add_name(message: types.Message):
    await message.answer('Enter the name of product')


@admin_router.message(F.text)
async def add_description(message: types.Message):
    await message.answer("Enter the description of product")


@admin_router.message(F.text)
async def add_price(message: types.Message):
    await message.answer('Enter the price of product')


@admin_router.message(F.text)
async def add_photo(message: types.Message):
    await message.answer('Please upload the photo for product')
    await message.answer('Product has been added =)')







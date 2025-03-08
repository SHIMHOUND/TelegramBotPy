from string import punctuation

from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from DictBad.bad_words import bad_words
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))
user_group_router.edited_message.filter(ChatTypeFilter(['supergroup', 'group']))

restricted_words = set(bad_words)


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def start_cmd(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.bot.send_message(message.from_user.id, f"You cannot use bad words in group!")
        await message.delete()
        # await message.chat.ban(message.from_user.id)

from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import (
    hbold, 
    hcode, 
    hpre, 
    hlink
)

from bot.misc import (
    i18n, 
    bot,
)
from bot.config import (
    ROOT_DIR,
    OWNER_ID,
)
from bot.keyboards import (
    example_inline,
    pagination_inline,
)
from bot.models import get_page_text
from bot.states import ExampleState


_ = i18n.gettext


async def start(msg: types.Message):
    text = _("Commands:")
    commands = "\n/lang\n/id\n/kb\n/pages\n/form\n/cancel"
    await msg.answer(text+commands)


async def lang(msg: types.Message, locale):
    await msg.answer(_('Your current lang: {lang}').format(lang=locale))


async def getid(msg: types.Message):
    await msg.answer(_("Your id: {id}").format(id=hcode(msg.from_user.id)))


async def keyboard(msg: types.Message):
    await msg.answer(_("Keyboard example"), 
        reply_markup=example_inline())


async def pagination(msg: types.Message):
    text, last = get_page_text()
    await msg.answer(text, reply_markup=pagination_inline(0, last))


async def cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('Canceled.', 
        reply_markup=types.ReplyKeyboardRemove())


async def form(msg: types.Message, state: FSMContext):
    await ExampleState.name.set()
    await msg.answer(_("Hi! What's your name?"))
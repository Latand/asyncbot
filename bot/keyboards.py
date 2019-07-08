from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
)
from bot.misc import i18n

from bot.utils import (
    example_cd,
    pagination_cd,
)


_ = i18n.gettext


def example_inline():
    markup = InlineKeyboardMarkup()
    url = InlineKeyboardButton('URL', url="telegram.org")
    cd = InlineKeyboardButton('CD', callback_data=example_cd.new('cd'))
    siqcc = InlineKeyboardButton('Inline', switch_inline_query_current_chat='Data')
    markup.add(cd, siqcc, url)
    return markup


def pagination_inline(page=0, last=0):
    if last <= 0: return
    back = page-1 if page > 0 else last
    forward = page+1 if page < last else 0
    b = InlineKeyboardButton('<', callback_data=pagination_cd.new(str(back)))
    f = InlineKeyboardButton('>', callback_data=pagination_cd.new(str(forward)))
    return InlineKeyboardMarkup().add(b, f)


def example_reply():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(_("Male"), _("Female"))
    return markup

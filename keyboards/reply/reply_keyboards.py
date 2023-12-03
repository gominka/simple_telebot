from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

EMPTY = ReplyKeyboardRemove()


def get_reply_keyboard(options, additional=None, **kwargs):
    row_width = kwargs.get("row_width", len(options))

    markup = ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    markup.add(*options, row_width=row_width)

    if additional:
        markup.add(*additional, row_width=len(additional))

    return markup

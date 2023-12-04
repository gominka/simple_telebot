from keyboa.keyboards import keyboa_maker
from loguru import logger
from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import BASE_PARAMS, conditions_list


@bot.callback_query_handler(func=lambda call: call.data in conditions_list(params=BASE_PARAMS,
                                                                           selected_condition="all_condition"))
@exc_handler
def call_btn_file(call: types.CallbackQuery) -> None:
    """Обработка нажатия кнопок, выбора условия"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    msg_user = call.data

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        cond = data["cond"]

        markup = types.InlineKeyboardMarkup(row_width=1)
        custom_search = types.InlineKeyboardButton(text='Поиск товаров', callback_data="check_len_responce")
        favourite = types.InlineKeyboardButton(text='Добавитьв избранное', callback_data="favourite")
        website = types.InlineKeyboardButton(text='Переход на сайт бренда', callback_data="website_link")
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_request')
        markup.add(custom_search, favourite)

        if cond == "brand":
            markup.add(website)

            data["params"]["brand"] = call.data
            logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {msg_user}')

        elif cond == "product_tag":
            data["params"]["product_tag"] = call.data
            logger.info(f'Выбран тэг. User_id: {user_id}, Product_tag: {msg_user}')

        elif cond == "product_type":
            data["params"]["product_type"] = call.data
            logger.info(f'Выбран тип продукта. User_id: {user_id}, Product_type: {msg_user}')

        markup.add(cancel)

        bot.send_message(chat_id=chat_id, text="Выберете опцию: ", reply_markup=markup)


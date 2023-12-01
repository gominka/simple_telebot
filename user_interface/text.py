from user_interface import emoji

MAIN_COMMANDS = f"\n\n {emoji.start_condition['brand']} /brand - Выбрать бренд" \
                f"\n\n {emoji.start_condition['product_tag']} /product_tag - Выбрать тэг" \
                f"\n\n {emoji.start_condition['product_type']} /product_type - Выбрать тип"

SEARCH_COMMANDS = f"\n\n{emoji.search_condition['high']} /high - Установить максимальную цену или рейтинг" \
                  f"\n\n{emoji.search_condition['low']} /low - Установить минимальную цену или рейтинг"

CUSTOM_COMMANDS = f"\n\n {emoji.start_condition['name']} /name - Поиск по имени" \
                  f"\n\n{emoji.addition_condition['add']} /add - Добавить в избранное"

FAV_COMMANDS = f"\n\n{emoji.addition_condition['favourite']} /favourite - Узнать добавление в избранное"

START_MSG = "Добро пожаловать в наш бот для поиска товаров!" \
            "\n\n Выберите условие для начала поиска: " + MAIN_COMMANDS

HELP_MSG = "Список доступных команд:" + MAIN_COMMANDS + FAV_COMMANDS

CONDITION = "Выберите команду:" + MAIN_COMMANDS + SEARCH_COMMANDS + CUSTOM_COMMANDS + FAV_COMMANDS

DESCRIPTION = "Описание товара:" \
              "{}" \
              "{}"

USER_HANDLER = "Что будем искать? " \
               "\n\n Напиши условие поиска."



START_OVER = "Начать поиск заново"

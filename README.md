# Telebot

## Краткое описание
Телеграмм-бот позволяет найти необходимое косметическое средство.
Пользователь может выполнить следующие действия:

## Описание команд

### Команда /start

   После выбора данной команды выводится сообщение, содержащее команды, необходимые для начала поиска, а также:
1. Если пользователь впервые пользуется ботом:
   - Пользователь заносится в базу данных
2. Если пользователь уже пользовался ботом:
   - в отправленном сообщении, добавляется команда, позволяющая посмотреть избранные параметры

### Команды /brand, /product_tag и /product_type

   После выбора одной из команд пользователь выбирает условие:
1. Самостоятельно ввести нужное условие
2. Продолжить поиск, выбрав условие из имеющихся атрибутов
3. После этого необходимо выбрать условие для продолжения поиска
   
### Команды /high, /low, /сustom

1. После выбора команды пользователь, с помощью кнопок выбирает: необходимо установить цену или рейтингу
2. Вводит выбранное число
3. После этого необходимо выбрать условие для продолжения поиска

### Команды /add

 
add - Добавить в избранное
favourite - Узнать добавление в избранное"
start_again
help

Запрос условий продолжает пока:
 - пользователь не выберет команду "/start_again" и начнет поиск заново
 - кол-во товаров, удовлетворяющий условия поиска не достигнет 5. Если так происходит, то пользователю выводится этот список

API Endpoint = http://makeup-api.herokuapp.com/api/v1/products.json
# Получение курса валют и генерация пользователей


1. Новый проект с виртуальным окружением
2. Модуль [*client.py*](client_.py). 
   * Функция, которая будет возвращать response по переданным `url` и `get params`. (Модуль requests установить через pip install)
   * Проверить с API получение [JSON](http://api.randomdatatools.ru)
   * Прописать отступы в [*config.py*](config_.py) и импортировать их.
   * Рассказать про порядок импорта модулей по PEP8 
3. Модуль [*parser.py*](parser_.py), который будет 
   * Парсить данные ЦБ о курсе валют по указанной дате; (GET params + datetime format. Формат даты хранить в [*config.py*](config_.py))
   * Конвертировать xml to dict (Модуль xmltodict установить средствами PyCharm)
   * Получить значение курса USD числом, а не строкой. 
4. Модуль config.py c настройкой формата даты
5. Модуль [*main.py*](main.py) 
   * Функция-генератор, которая выдает случайный пользователей из API (см. 3.2)
   * Сформировать список людей из функции-генератора
   * Добавить поле `salary_rub` с зарплатой конвертированной в рубли по курсу на указанную дату.
   * Добавить декоратор `lru_cache`, который будет кешировать значения курса.
   * Записать список людей в JSON файл. 
6. Сохранить зависимости в файл [*requirements.txt*](requirements.txt)
7. Оформить [README.md](README.MD)

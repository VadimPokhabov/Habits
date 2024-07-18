# Приложение "Habits" трекер полезных привычек
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к нам с запросом реализовать трекер полезных привычек.
В рамках учебного курсового проекта реализована бэкенд-часть SPA веб-приложения.
____
 Приложение выполнено на Django REST framework
### Стек:
* Django
* Django REST framework
* Celery
* Django-filter
* Swagger
* redoc
* django-celery-beat
* drf-yasg
* CORS
* redis
* psycopg2 (ORM)
* telegram-bot
____
Данное приложение работает на взаимодействие API.
Пользователь регистрируется, затем, добавляет свою привычку и время ее выполнения.
____
После заполнения данными, пользователь в праве выбрать, как часто напоминать о привычки (раз в день или раз в неделю. Поле 'is_daily' где 'True' - раз в день, 'False' - раз в неделю).
Так же пользователь может выбрать в качестве награды, кастомную (свою личную привычку в поле 'prize') либо сослаться на приятную привычку (если ее создать. Поле 'related' - ID приятной привычки).
____
Для запуска проекта у себя локально необходимо:

1. git clone репозитория
```
git@github.com:VadimPokhabov/Habits.git
```
2. Установить виртуальное окружение venv
```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```
3. Активировать виртуальное окружение
```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```
4. установить файл с зависимостями
```
pip install -r requirements.txt
```
5. Создать базу данных в PgAdmin, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'base' в константе (словаре) 'DATABASES'
6. Заполнить своими данными файл .env в корне вашего проекта. Образец файла лежит в корне .env.sample
7. Для запуска проекта использовать команду
```
python manage.py ruserver
```
8. Для запуска celery work и celery beat используйте команду
```
-A base worker --beat --scheduler django --loglevel=info
```
____
### Важно:
### При регистрации пользователя, необходимо указать свой ID телеграм. Иначе регистрация не получится.
____
### Внимание
#### Чтобы приложение работало хорошо, сравните свой часовой пояс с текущим в приложение, если он не совпадает, поменяйте его на свой в приложение base/settings UTC

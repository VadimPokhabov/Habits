# Приложение "Habits" трекер полезных привычек
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к нам с запросом реализовать трекер полезных привычек.
В рамках учебного курсового проекта реализована бэкенд-часть SPA веб-приложения.
____
 Приложение выполнено на Django REST framework
### Стек:
* Django
* Django REST framework
* Celery
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
Запуск приложения через Docker:

1. Повторить шаги 1-3
2. Запустить Docker локально на машине
3. Выполнить команду в терминале
```
docker compose up -d --build
```
Данная команда сразу создаст образ, и сбилдит его, т.е. запустит локально в Docker

4. Переходим по ссылке http://localhost:8000/
----
Чтобы удалить контейнеры после работы с приложением используйте команду
```
docker-compose down
```
----
Деплой приложения на удаленный сервер в ручном режиме.

1. Необходимо установить зависимости на удаленный сервер
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib python3-pip
apt install gunicorn
apt install nginx
```
2. Необходимо установить виртуальное окружение на удаленном сервере
```
python3 -m venv venv
```
3. Активировать виртуальное окружение
```
source venv/bin/activate
```
4. Скопировать свой проект на сервер
```
git clone <ssh вашего проекта с гит>
```
5. Установить все зависимости с файла requirements.txt
```
pip install -r requirements.txt
```
6. Настроить демон (gunicorn) на удаленном сервере yourproject.service и добавить данные в файл
```
[Unit]
Description=gunicorn daemon for Your Project # Описание вашего сервиса
After=network.target # Сервис, от которого будет зависеть запуск проекта

[Service]
User=yourusername # Имя пользователя владельца проекта в Linux
Group=yourgroupname # Группа, к которой относится пользователь
WorkingDirectory=/path/to/your/project # Путь к рабочей директории проекта
ExecStart=/path/to/venv/bin/gunicorn --config /path/to/gunicorn_config.py your_project.wsgi:application
# Команда для запуска проекта
```
7. Запустите сервис
```
sudo systemctl start yourproject
```
8. Настройка Nginx сервера для работы со статикой вашего проекта /etc/nginx/sites-available/my_site
```
server {
    listen 80;
    server_name <ip адрес или доменное имя сервера>;

    location /static/ {
			root /path/to/your/project/;
    }

    location /media/ {
			root /path/to/your/project/;
    }

    location / {
			include proxy_params;
			proxy_pass /path/to/your/project/project.sock
    }

}
```

9. Командой nginx -t проверяйте корретность заполнения файла
10. Подключите сайт к отображению
```
ln -s /etc/nginx/sites-available/my_site /etc/nginx/sites-enabled
```
11. Выполнить команду для определение статики проекта
```
python3 manage.py collectstatic
```
----
Деплой приложения череез Docker на удаленный сервер

1. Выполнить шаги 1,3,5,6,7,8
2. Установить docker и docker-compose на удаленный сервер
```
apt install docker docker-compose
```
3. Выполнить команду
```
docker compose up -d --build
```
----
Подключение CI/CD
1. Регистрируемся на GitLab
2. Клонируем проект себе в GitLab используя SSH ключ
```
git@github.com:VadimPokhabov/Habits.git
```
3. В разделе settings -> CI/CD -> Runners создаем runner
4. В разделе settings -> CI/CD -> Variables создаем env файл для взаимодействия с проектом
5. Выполнить установку у себя на удаленном сервере
```
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash
sudo -E apt-get install gitlab-runner
```
____
### Важно:
### При регистрации пользователя, необходимо указать свой ID телеграм. Иначе регистрация не получится.
____
### Внимание
#### Чтобы приложение работало хорошо, сравните свой часовой пояс с текущим в приложение, если он не совпадает, поменяйте его на свой в приложение base/settings UTC

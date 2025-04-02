#!/bin/sh

# Выполняем миграции
poetry run python manage.py makemigrations
poetry run python manage.py migrate

# Запускаем сервер
exec poetry run python manage.py runserver 0.0.0.0:8000

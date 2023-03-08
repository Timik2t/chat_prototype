# Проект Private_chat

## Проект в разработке.
___

## Описание

Основные идеи

- Создать веб чат используя библеотеку 'django private chat'
- Добавть чат бота
- реализовать поддержку Markdown 

## Технологии

Django 3.2.6

django-private-chat 0.3.0

PostgreSQL 

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone git@github.com:Timik2t/chat_prototype.git
```
* Cоздайте .env файл и впишите:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=5432
    
    DJANGO_KEY=<секретный ключ проекта django>
    ```


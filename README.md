✏️ Веб-приложение для общения с людьми

![Иллюстрация к проекту](https://github.com/Acejkee/images/blob/main/Real_time_chat/home.png)
![Иллюстрация к проекту](https://github.com/Acejkee/images/blob/main/Real_time_chat/log_in.png)
![Иллюстрация к проекту](https://github.com/Acejkee/images/blob/main/Real_time_chat/rooms.png)
![Иллюстрация к проекту](https://github.com/Acejkee/images/blob/main/Real_time_chat/room.png)



Это веб-приложение предоставляет платформу для общения c другими пользователями. Вы можете общаться в личных беседах и участвовать в групповых дискуссиях. Администратор приложения имеет возможность создавать и управлять группами, обеспечивая организованное и тематическое общение.

✏️ Технологии

Приложение построено на современных технологиях, обеспечивающих высокую производительность и надежность:

- **Backend**: Django, Django Channels
- **Async Server**: Daphne
- **Database**: PostgreSQL
- **Frontend**: Tailwind CSS
- **Контейнеризация**: Docker, Docker Compose


✏️ Установка и запуск

1. Скопируйте файл .env.example в .env и заполните его своими данными.
2. Запустите приложение, используя Docker Compose:

```bash
docker compose up -d --build
```

После запуска приложение будет доступно по адресу: http://localhost:8000

✏️ Клонирование репозитория

Вы можете клонировать репозиторий приложения с помощью следующей команды:

```bash
git clone https://github.com/Acejkee/Real_time_chat
```
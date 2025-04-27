# Time Tracker API

Микросервис для учета рабочего времени с REST API интерфейсом. Учет пользователей, проектов и отработанных часов.

## Технологии
- Python 3.11
- FastAPI (веб-фреймворк)
- SQLAlchemy (ORM)
- Pydantic (валидация)
- PostgreSQL/SQLite (БД)
- Docker (контейнеризация)
- Pytest (тестирование)
- Just (управление задачами)

## Запуск (Windows)
1. Установите [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Скачайте и распакуйте проект
3. В PyCharm:
   - Откройте проект
   - Создайте виртуальное окружение: `python -m venv venv`
   - Активируйте его
4. Запустите сервис: `just up`

Приложение будет доступно на `http://localhost:8000` с автоматической документацией:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Основные команды
- `just up` - запуск сервиса
- `just test` - запуск тестов
- `just lint` - проверка кода
- `just format` - форматирование кода
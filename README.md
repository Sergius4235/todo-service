# To-Do List Service

Цей проєкт реалізує веб-сервіс To-Do List за допомогою FastAPI, PostgreSQL та Docker.

## Інструкція з запуску

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/Sergius4235/todo-service.git
   cd todo-service
   ```
2. Запустіть сервіс за допомогою Docker:
   ```bash
   docker-compose up --build
   ```
3. API буде доступне за адресою `http://localhost:8000`

## Опис API

- `GET /tasks` - Отримати список завдань
- `GET /auth/login` - Симуляція аутентифікації

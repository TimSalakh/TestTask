# Запуск проекта

## Запуск проекта

Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Запуск с Docker compose

```bash
docker-compose up --build
```

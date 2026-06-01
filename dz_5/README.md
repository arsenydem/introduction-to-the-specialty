# ДЗ 5 — Тестирование (unit / functional / e2e)

Небольшое API задач на **FastAPI** (логика из **dz_2** / **dz_3**) и три уровня автотестов.

## Типы тестов

| Тип | Папка | Что проверяет |
|-----|--------|----------------|
| **Unit** | `tests/unit/` | `greet()`, `TaskStore`, валидация — без HTTP и браузера |
| **Functional** | `tests/functional/` | REST API через `TestClient` (в памяти, без сети) |
| **E2E** | `tests/e2e/` | Реальный `uvicorn` + **Playwright** (страница и `fetch`) |

## CI

Workflow [`.github/workflows/dz5-tests.yml`](../.github/workflows/dz5-tests.yml) на Pull Request:

1. **Unit tests**
2. **Functional tests**
3. **E2E tests** (после unit и functional)

## Локальный запуск

```bash
cd dz_5
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
playwright install chromium

pytest tests/unit -m unit -q
pytest tests/functional -m functional -q
pytest tests/e2e -m e2e -q
```

Все сразу:

```bash
pytest -q
```

Запуск приложения вручную:

```bash
uvicorn dz5.app:app --reload --port 8000
```

Открыть: http://127.0.0.1:8000

## Соответствие критериям

| Баллы | Что сделано |
|-------|-------------|
| 6/10 | Рабочие unit + functional |
| 8/10 | CRUD задач, greet, фильтры, ошибки 400/404 |
| 10/10 | Три типа тестов + отдельные job'ы в GitHub Actions |

## Сдача

Ветка → `git add dz_5 .github/workflows/dz5-tests.yml` → PR → ссылка в таблицу курса.

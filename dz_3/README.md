# ДЗ 3 — CI pipeline (GitHub Actions)

Небольшой Python-проект с автоматическими проверками при Pull Request.

## Что проверяет CI

| Job | Проверка |
|-----|----------|
| **Lint** | `ruff check` — стиль и ошибки кода |
| **Format** | `ruff format --check` — единое форматирование |
| **Tests** | `pytest` — юнит-тесты (запускается после lint и format) |

Workflow: [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)

## Локальный запуск (перед PR)

```bash
cd dz_3
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
ruff check src tests
ruff format --check src tests
pytest -q
```

Исправить форматирование: `ruff format src tests`

## Как сдать

1. Создайте ветку, например `feature/dz3-ci`.
2. Закоммитьте изменения в `dz_3/` и `.github/workflows/ci.yml`.
3. Запушьте ветку и откройте **Pull Request** в `main`.
4. Дождитесь зелёных проверок в PR (вкладка **Checks**).
5. Скопируйте ссылку на PR и вставьте в таблицу курса.

## 10/10: блокировка merge при ошибках

В GitHub: **Settings → Branches → Branch protection rules** для `main`:

- включить **Require a pull request before merging**;
- включить **Require status checks to pass before merging**;
- отметить обязательные checks: `Lint (Ruff)`, `Format (Ruff)`, `Tests (pytest)`.

После этого merge в `main` будет возможен только при успешном CI.

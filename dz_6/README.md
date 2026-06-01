# ДЗ 6 — Статический анализ безопасности (Semgrep)

Проверка кода на уязвимости и плохие практики **до** деплоя. Основа — исправленное приложение в `src/dz6/`; учебные примеры ошибок — в `training/`.

## Инструмент

**Semgrep** — правила из сообщества (`p/python`, `p/secrets`, OWASP).

Установка:

```bash
pip install semgrep
# или: https://semgrep.dev/docs/getting-started/
```

## Запуск анализа

```bash
cd dz_6

# Код приложения (как в CI) — ожидается 0 findings
semgrep scan --config p/python --config p/secrets --config p/owasp-top-ten src/

# Учебные уязвимости — будут findings (для отчёта)
semgrep scan --config p/python --config p/secrets training/
```

JSON-отчёт:

```bash
semgrep scan --config p/python --config p/secrets src/ --json -o semgrep-report.json
```

## CI

При изменении `dz_6/` в Pull Request запускается [dz6-semgrep.yml](../.github/workflows/dz6-semgrep.yml):

- сканируется `src/`;
- при findings pipeline **падает** (quality gate);
- `training/` исключён через `.semgrepignore`.

## Разбор issues (10/10)

Подробная таблица «было → стало»: [docs/semgrep-review.md](docs/semgrep-review.md)

## Тесты приложения

```bash
pip install -r requirements-dev.txt
pytest -q
```

Запуск API (нужен `API_KEY`):

```bash
set API_KEY=dev-local-key
uvicorn dz6.app:app --reload --port 8000
```

## Критерии

| Баллы | Реализация |
|-------|------------|
| 6/10 | `semgrep scan` на `src/`, результаты в CI |
| 8/10 | проблемы исправлены в `src/dz6/` |
| 10/10 | CI + [semgrep-review.md](docs/semgrep-review.md) |

## Сдача

```bash
git checkout -b feature/dz6-semgrep
git add dz_6 .github/workflows/dz6-semgrep.yml
git commit -m "dz_6: Semgrep SAST and security fixes"
git push -u origin feature/dz6-semgrep
```

Ссылка на PR — в таблицу курса.

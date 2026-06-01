# Onboarding: передача проекта разработчику

Добро пожаловать в репозиторий **introduction-to-the-specialty**. Этот файл — точка входа, если вы получили проект «как есть».

## 1. Что это за проект

Учебный **Task Manager** (список задач с REST API и веб-интерфейсом), собранный в нескольких итерациях (`dz_2` … `dz_7`). Полное описание — в [PROJECT_REPORT.md](PROJECT_REPORT.md).

## 2. С чего начать (15 минут)

```bash
git clone https://github.com/arsenydem/introduction-to-the-specialty.git
cd introduction-to-the-specialty
```

### Вариант A — Python (рекомендуется)

```bash
cd dz_5
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
playwright install chromium
pytest -q
uvicorn dz5.app:app --reload --port 8000
```

Откройте http://127.0.0.1:8000

### Вариант B — Docker (Node)

```bash
cd dz_4
docker build -t todo-app:dz4 .
docker run --rm -p 3000:3000 todo-app:dz4
```

Откройте http://localhost:3000

## 3. Где что лежит

| Вопрос | Путь |
|--------|------|
| Исходный Node API | `dz_2/server.js` |
| Тесты | `dz_5/tests/` |
| Dockerfile | `dz_4/Dockerfile` |
| CI workflows | `.github/workflows/` |
| Semgrep / безопасность кода | `dz_6/` |
| SBOM / Trivy | `dz_7/` |
| Финальный отчёт | `dz_8/docs/PROJECT_REPORT.md` |

## 4. Как вносить изменения

1. Ветка от `main`: `git checkout -b feature/my-change`
2. Правки в нужной папке `dz_*`
3. Локально прогнать тесты (см. README папки)
4. `git push` → **Pull Request**
5. Дождаться зелёных GitHub Actions

Токен GitHub для push workflow-файлов должен иметь scope **`workflow`**.

## 5. Частые проблемы

| Симптом | Решение |
|---------|---------|
| `git add dz_3` не работает из папки `dz_3` | Выполнять `git add` из **корня** репозитория |
| Push workflow отклонён | Добавить scope `workflow` в PAT |
| E2E падает локально | `playwright install chromium` |
| Trivy/Syft не найдены | Установить CLI или смотреть артефакты CI |

## 6. Контакты и сдача

Сдача домашних — ссылка на PR в таблице курса.  
Технические решения — [ADR-001-tech-stack.md](ADR-001-tech-stack.md).

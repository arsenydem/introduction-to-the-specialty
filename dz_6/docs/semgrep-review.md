# Разбор Semgrep (dz_6)

Инструмент: **[Semgrep](https://semgrep.dev/)** — статический анализ на этапе разработки (SAST).

## Как запускать

**Продакшен-код** (должен быть без findings — так и настроен CI):

```bash
cd dz_6
semgrep scan --config p/python --config p/secrets --config p/owasp-top-ten src/
```

**Учебные уязвимости** (папка `training/`, в CI исключена):

```bash
semgrep scan --config p/python --config p/secrets training/
```

## Найденные проблемы и исправления

| # | Правило Semgrep (пример) | Было (плохая практика) | Стало (исправление) | Файл |
|---|--------------------------|------------------------|---------------------|------|
| 1 | `python.lang.security.audit.hardcoded-secret` | Пароль/API key в коде | `os.environ["API_KEY"]`, ошибка если не задан | `src/dz6/auth.py` |
| 2 | `python.lang.security.audit.sql-injection` | `f"SELECT ... '{user}'"` | Плейсхолдеры `?` в sqlite3 | `src/dz6/database.py` |
| 3 | `python.lang.security.audit.dangerous-eval` | `eval(user_input)` | `json.loads()` для данных | `src/dz6/utils.py` |
| 4 | `python.lang.security.audit.insecure-hash` | `hashlib.md5(password)` | (убрано; в API нет хранения паролей в MD5) | — |
| 5 | `subprocess` + `shell=True` | `subprocess.call(..., shell=True)` | (не используем shell в приложении) | — |

### 1. Секреты в репозитории

**Риск:** ключ в git → утечка при публикации репозитория, сканировании форков.

**Исправление:** секрет только в переменных окружения / CI secrets (`API_KEY` в GitHub Actions для тестов).

### 2. SQL injection

**Риск:** подстановка строки в SQL позволяет выполнить произвольный запрос (`' OR 1=1 --`).

**Исправление:** параметризованные запросы — СУБД отделяет данные от кода запроса.

### 3. eval() на пользовательском вводе

**Риск:** выполнение произвольного Python-кода.

**Исправление:** парсинг JSON для структурированных данных; для кода — никогда не использовать `eval` на внешнем вводе.

## Пример вывода Semgrep (training/)

При сканировании `training/insecure_snippets.py` типично появляются предупреждения уровня **ERROR** / **WARNING**, например:

- hardcoded secret в `API_KEY = "..."`
- `eval(expression)`
- SQL через f-string
- `hashlib.md5` для паролей
- `subprocess` с `shell=True`

Это ожидаемо: файл создан **только для демонстрации** срабатываний.

## Вывод для разработки

1. SAST в CI ловит типовые ошибки **до** merge.
2. Секреты — в окружении, не в коде.
3. Запросы к БД — только с параметрами.
4. Не выполнять пользовательский ввод как код (`eval`, `exec`, `shell=True`).

CI workflow: [`.github/workflows/dz6-semgrep.yml`](../../.github/workflows/dz6-semgrep.yml)

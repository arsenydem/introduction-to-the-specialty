# ДЗ 4 — Docker

To-Do приложение из **dz_2**, упакованное в контейнер: изолированное окружение и одинаковый запуск на любой машине.

## Требования

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (или Docker Engine + CLI)

## Сборка образа

Из папки `dz_4`:

```bash
docker build -t todo-app:dz4 .
```

**Структура Dockerfile (8/10):**

1. **deps** — сначала только `package.json`, затем `npm install` (слой кэшируется при изменении только кода).
2. **runner** — Alpine-образ без dev-зависимостей, отдельный непривилегированный пользователь `app`.

Опционально для ещё более воспроизводимой сборки скопируйте `package-lock.json` из `dz_2` и замените в Dockerfile `npm install` на `npm ci`.

## Запуск контейнера

```bash
docker run --rm -p 3000:3000 --name todo-dz4 todo-app:dz4
```

| Параметр | Значение |
|----------|----------|
| Порт | `3000` на хосте → `3000` в контейнере |
| `--rm` | удалить контейнер после остановки (`Ctrl+C`) |

Откройте в браузере: **http://localhost:3000**

Проверка API:

```bash
curl http://localhost:3000/api/tasks
```

Другой порт на хосте:

```bash
docker run --rm -p 8080:3000 -e PORT=3000 todo-app:dz4
```

## Полезные команды

```bash
# список образов
docker images todo-app

# логи работающего контейнера
docker logs todo-dz4

# остановить
docker stop todo-dz4
```

## Размер образа (10/10)

Multi-stage + `node:22-alpine` + только production-зависимости:

```bash
docker images todo-app:dz4
```

Ожидаемо ~150–200 MB (без devDependencies и без исходников сборки в финальном слое).

## Сдача

1. Ветка → коммит `dz_4/` → push → Pull Request (как в dz_3).
2. В таблицу — ссылка на PR.

Локально перед PR:

```bash
cd dz_4
docker build -t todo-app:dz4 .
docker run --rm -p 3000:3000 todo-app:dz4
```

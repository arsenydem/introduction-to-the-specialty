# ДЗ 8 — Финальный отчёт по проекту

Документация для сдачи и передачи проекта другому разработчику.

## Главный документ

**[docs/PROJECT_REPORT.md](docs/PROJECT_REPORT.md)** — полный отчёт:

- описание системы;
- архитектура;
- этапы разработки (dz_2 … dz_7);
- тестирование;
- безопасность;
- эксплуатация и CI/CD;
- выводы.

## Дополнительно

| Документ | Назначение |
|----------|------------|
| [docs/ONBOARDING.md](docs/ONBOARDING.md) | Быстрый старт для нового разработчика |
| [docs/ADR-001-tech-stack.md](docs/ADR-001-tech-stack.md) | Ключевые технические решения |

## CI для dz_8

Только проверка документов: [`.github/workflows/dz8-docs.yml`](../.github/workflows/dz8-docs.yml)  
**Без Trivy** — отчёт сдаётся как Markdown.

## Сдача

1. Ветка `feature/dz8-report` → `git add dz_8 .github/workflows/dz8-docs.yml`
2. Pull Request в `main`
3. Ссылка на PR — в таблицу курса

Проверяющему: `dz_8/docs/PROJECT_REPORT.md` + зелёный workflow **dz8 Docs**.

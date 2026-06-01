# ДЗ 7 — SBOM и сканирование зависимостей

Анализ **сторонних библиотек**: состав (SBOM) и известные уязвимости (CVE).

## Инструменты

| Инструмент | Назначение |
|------------|------------|
| [Syft](https://github.com/anchore/syft) | SBOM (CycloneDX / SPDX) |
| [Trivy](https://github.com/aquasecurity/trivy) | Поиск CVE в зависимостях |

Установка: см. официальные инструкции или `choco install syft trivy` (Windows).

## Быстрый старт

```powershell
cd dz_7
pip install -r requirements-dev.txt

# Скан (нужны syft и trivy в PATH)
.\scripts\scan-deps.ps1
```

Результаты:

- `sbom/sbom.cyclonedx.json` — SBOM  
- `reports/trivy-table.txt` — таблица уязвимостей  

## CI

Workflow [dz7-sbom-trivy.yml](../.github/workflows/dz7-sbom-trivy.yml):

1. **SBOM** — Syft, артефакт в Actions  
2. **Trivy** — fail при HIGH/CRITICAL с доступным фиксом  
3. **pytest** — smoke-тест приложения  

## Разбор уязвимостей (8–10/10)

Подробный отчёт: [docs/vulnerability-report.md](docs/vulnerability-report.md)

- что было небезопасно;  
- какие CVE/риски;  
- **что обновлено** в `requirements.txt`.

## Критерии

| Баллы | Реализация |
|-------|------------|
| 6/10 | SBOM + отчёт Trivy (локально или артефакт CI) |
| 8/10 | [vulnerability-report.md](docs/vulnerability-report.md) |
| 10/10 | обновлённые версии в `requirements.txt` + CI |

## Сдача

```bash
git checkout -b feature/dz7-sbom-trivy
git add dz_7 .github/workflows/dz7-sbom-trivy.yml
git commit -m "dz_7: Syft SBOM and Trivy dependency scanning"
git push -u origin feature/dz7-sbom-trivy
```

Ссылка на PR — в таблицу курса.

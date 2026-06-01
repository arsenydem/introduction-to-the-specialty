# ДЗ 7 — SBOM и зависимости (на 8/10)

## Что сдаём

| Критерий | Где |
|----------|-----|
| SBOM | CI → артефакт `dz7-security-reports` → `sbom.cyclonedx.json` |
| Отчёт по CVE | тот же артефакт → `trivy-table.txt` + [docs/vulnerability-report.md](docs/vulnerability-report.md) |
| CI | [.github/workflows/dz7-sbom-trivy.yml](../.github/workflows/dz7-sbom-trivy.yml) — **зелёный** |

Разбор уязвимостей (было / стало / риск) — в **vulnerability-report.md**, не обязательно ломать CI из‑за каждого CVE.

## Локально (по желанию)

```powershell
cd dz_7
pip install -r requirements-dev.txt
pytest -q
```

Syft/Trivy — те же команды, что в workflow (нужен Docker).

## Сдача

PR с `dz_7/` + workflow → ссылка в таблицу курса.

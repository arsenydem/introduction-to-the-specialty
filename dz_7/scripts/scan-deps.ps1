# Локальный скан: SBOM (Syft) + Trivy (отчёт)
$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)
New-Item -ItemType Directory -Force -Path sbom, reports | Out-Null

syft scan dir:. -o cyclonedx-json | Out-File -Encoding utf8 sbom/sbom.cyclonedx.json
trivy fs . --scanners vuln --format table --exit-code 0 --output reports/trivy-table.txt
Write-Host "Done: sbom/ reports/"

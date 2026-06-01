# Локальный скан: SBOM (Syft) + уязвимости (Trivy)
# Требуется: syft, trivy в PATH

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

New-Item -ItemType Directory -Force -Path sbom, reports | Out-Null

Write-Host "==> Syft: SBOM (CycloneDX)" -ForegroundColor Cyan
syft scan dir:. -o cyclonedx-json | Out-File -Encoding utf8 sbom/sbom.cyclonedx.json

Write-Host "==> Trivy: vulnerabilities" -ForegroundColor Cyan
trivy fs . --config .trivy.yaml --format table --output reports/trivy-table.txt
trivy fs . --config .trivy.yaml --format json --output reports/trivy.json

Write-Host "Done. See sbom/ and reports/" -ForegroundColor Green

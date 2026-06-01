#!/usr/bin/env bash
# SBOM (Syft) + Trivy — Linux/macOS/Git Bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p sbom reports

echo "==> Syft: SBOM"
syft scan dir:. -o cyclonedx-json > sbom/sbom.cyclonedx.json

echo "==> Trivy: vulnerabilities"
trivy fs . --config .trivy.yaml --format table -o reports/trivy-table.txt
trivy fs . --config .trivy.yaml --format json -o reports/trivy.json

echo "Done. See sbom/ and reports/"

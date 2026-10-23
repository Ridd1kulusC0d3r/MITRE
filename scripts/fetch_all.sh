#!/usr/bin/env bash
# fetch_all.sh — baixa versões FIXAS dos dados MITRE para data/cache/ e grava
# um manifesto com SHA-256 (cadeia de custódia simples). Requer curl e sha256sum.
#
#   ./scripts/fetch_all.sh                 # ATT&CK 20.0 + CAPEC + ATLAS 2026.09
#   ATTACK_VERSION=19.2 ATLAS_VERSION=2026.06 ./scripts/fetch_all.sh
#   D3FEND=1 ./scripts/fetch_all.sh        # inclui mapeamentos D3FEND (arquivo grande)
#
# data/cache/ está no .gitignore: os bundles não vão para o repositório.
set -euo pipefail

ATTACK_VERSION="${ATTACK_VERSION:-20.0}"
D3FEND_VERSION="${D3FEND_VERSION:-1.6.0}"
# dist/ATLAS-latest.yaml é um symlink no Git (o raw devolve só o caminho); use o arquivo versionado
ATLAS_VERSION="${ATLAS_VERSION:-2026.09}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/data/cache"
mkdir -p "$OUT"

RAW=https://raw.githubusercontent.com
declare -a SOURCES=(
  "enterprise-attack-$ATTACK_VERSION.json|$RAW/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-$ATTACK_VERSION.json"
  "mobile-attack-$ATTACK_VERSION.json|$RAW/mitre-attack/attack-stix-data/master/mobile-attack/mobile-attack-$ATTACK_VERSION.json"
  "ics-attack-$ATTACK_VERSION.json|$RAW/mitre-attack/attack-stix-data/master/ics-attack/ics-attack-$ATTACK_VERSION.json"
  "stix-capec.json|$RAW/mitre/cti/master/capec/2.1/stix-capec.json"
  "ATLAS-$ATLAS_VERSION.yaml|$RAW/mitre-atlas/atlas-data/main/dist/v6/ATLAS-$ATLAS_VERSION.yaml"
)
if [[ "${D3FEND:-0}" == "1" ]]; then
  SOURCES+=("d3fend-full-mappings-$D3FEND_VERSION.json|https://d3fend.mitre.org/ontologies/d3fend/$D3FEND_VERSION/d3fend-full-mappings.json")
fi

MANIFEST="$OUT/manifest.tsv"
printf 'arquivo\tsha256\tbytes\tbaixado_em_utc\turl\n' > "$MANIFEST"
for item in "${SOURCES[@]}"; do
  name="${item%%|*}"; url="${item#*|}"
  printf '→ %s\n' "$name"
  if ! curl -fsSL --retry 3 --max-time 600 -o "$OUT/$name.part" "$url"; then
    printf '  ✗ falhou: %s\n' "$url" >&2; rm -f "$OUT/$name.part"; continue
  fi
  mv "$OUT/$name.part" "$OUT/$name"
  sum=$(sha256sum "$OUT/$name" | cut -d' ' -f1)
  size=$(wc -c < "$OUT/$name" | tr -d ' ')
  printf '%s\t%s\t%s\t%s\t%s\n' "$name" "$sum" "$size" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$url" >> "$MANIFEST"
  printf '  ✓ %s bytes  sha256=%s…\n' "$size" "${sum:0:16}"
done
printf '\nManifesto: %s\n' "$MANIFEST"

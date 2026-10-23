#!/usr/bin/env bash
# jq-receitas.sh — consultas rápidas no bundle STIX do ATT&CK com jq.
# Uso: ./scripts/jq-receitas.sh <receita> [arquivo]
#   arquivo padrão: data/cache/enterprise-attack-20.0.json (rode fetch_all.sh antes)
#
# Receitas:
#   contagem        objetos ativos por tipo
#   taticas         ID e nome das táticas
#   impairment      técnicas da tática Defense Impairment (TA0112)
#   stealth         técnicas da tática Stealth (TA0005)
#   ia              técnicas que citam IA/LLM/prompt no nome
#   grupo NOME      técnicas usadas por um grupo (ex.: grupo APT29)
#   revogadas       técnicas revogadas e suas substitutas
set -euo pipefail
R="${1:-}"; shift || true
F="${F:-data/cache/enterprise-attack-20.0.json}"
[[ "${1:-}" == *.json ]] && { F="$1"; shift; }
[[ -f "$F" ]] || { echo "Arquivo $F não encontrado. Rode ./scripts/fetch_all.sh" >&2; exit 1; }

ACTIVE='select((.revoked|not) and (.x_mitre_deprecated|not))'
EID='(.external_references[]|select(.source_name=="mitre-attack").external_id)'

case "$R" in
  contagem)
    jq "[.objects[]|$ACTIVE]|group_by(.type)|map({tipo:.[0].type,n:length})" "$F";;
  taticas)
    jq -r ".objects[]|select(.type==\"x-mitre-tactic\")|$ACTIVE|[$EID,.name]|@tsv" "$F" | sort;;
  impairment|stealth)
    phase=$([[ "$R" == impairment ]] && echo defense-impairment || echo stealth)
    jq -r ".objects[]|select(.type==\"attack-pattern\")|$ACTIVE
      |select(any(.kill_chain_phases[]?;.phase_name==\"$phase\"))|[$EID,.name]|@tsv" "$F" | sort;;
  ia)
    jq -r ".objects[]|select(.type==\"attack-pattern\")|$ACTIVE|select(.name|test(\"AI|LLM|Prompt\"))|[$EID,.name]|@tsv" "$F" | sort;;
  grupo)
    G="${1:?informe o nome do grupo}"
    jq -r --arg g "$G" '
      (.objects|map({key:.id,value:.})|from_entries) as $by
      | ([.objects[]|select(.type=="intrusion-set" and (.name==$g or ((.aliases//[])|index($g))))|.id]) as $ids
      | .objects[]|select(.type=="relationship" and .relationship_type=="uses" and (.source_ref as $s|$ids|index($s)))
      | $by[.target_ref]|select(.type=="attack-pattern")
      | [(.external_references[]|select(.source_name=="mitre-attack").external_id),.name]|@tsv' "$F" | sort -u;;
  revogadas)
    jq -r '
      (.objects|map({key:.id,value:.})|from_entries) as $by
      | .objects[]|select(.type=="relationship" and .relationship_type=="revoked-by")
      | [$by[.source_ref],$by[.target_ref]]|select(.[0].type=="attack-pattern")
      | [(.[0].external_references[]|select(.source_name=="mitre-attack").external_id),
         "→",(.[1].external_references[]|select(.source_name=="mitre-attack").external_id),.[1].name]|@tsv' "$F" | sort;;
  *)
    sed -n '2,15p' "$0"; exit 1;;
esac

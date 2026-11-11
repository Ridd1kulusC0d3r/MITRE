#!/usr/bin/env python3
"""merge_legacy.py — consolida data/ecosystem.json de várias branches, por id.

Uso descartável da Fase 0 do PLANO-REFATORACAO.md. Somente stdlib.

    python3 scripts/merge_legacy.py BASE_REF REF [REF ...] > relatorio.md

Regras:
- a base fornece o ponto de partida;
- entrada ausente na base e presente numa branch é adicionada;
- campo ausente ou vazio na base e preenchido na branch: entra sempre;
- campo divergente: vence o valor da entrada com `reviewed_on` mais recente;
  empate com valores diferentes vai para revisão manual (mantém o da base);
- `historical`, `repository_checks` e `mitre_attack_archived`: união por nome/url;
- metadados globais: maior `reviewed_on`; demais chaves da base.
Grava o resultado em data/ecosystem.json e imprime o relatório em Markdown.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(ref):
    raw = subprocess.run(["git", "show", f"{ref}:data/ecosystem.json"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    return json.loads(raw)


def short(v, n=70):
    s = json.dumps(v, ensure_ascii=False)
    return s if len(s) <= n else s[:n - 1] + "…"


def union(base, extra, key):
    seen = {key(x) for x in base}
    added = [x for x in extra if key(x) not in seen]
    return base + added, added


def main():
    base_ref, refs = sys.argv[1], sys.argv[2:]
    out = load(base_ref)
    by_id = {e["id"]: e for e in out["entries"]}
    origin = {i: base_ref for i in by_id}
    log, review = [], []
    for ref in refs:
        d = load(ref)
        changes = []
        for e in d["entries"]:
            cur = by_id.get(e["id"])
            if cur is None:
                by_id[e["id"]] = dict(e)
                origin[e["id"]] = ref
                changes.append(f"+ {e['id']} {e['name']} (nova)")
                continue
            for k in sorted(set(e) | set(cur)):
                a, b = cur.get(k), e.get(k)
                if a == b or k == "reviewed_on":
                    continue
                ra, rb = cur.get("reviewed_on", ""), e.get("reviewed_on", "")
                if a in (None, "", []) and b not in (None, "", []):
                    cur[k] = b  # campo ausente na base: sempre preenche
                    changes.append(f"+ {e['id']}.{k} = {short(b)} (preenchido)")
                elif rb > ra:
                    cur[k] = b
                    changes.append(f"~ {e['id']}.{k}: {short(a)} → {short(b)}")
                elif rb == ra:
                    review.append(f"{e['id']}.{k}: base {short(a)} × {ref} {short(b)}")
            if e.get("reviewed_on", "") > cur.get("reviewed_on", ""):
                cur["reviewed_on"] = e["reviewed_on"]
        for key, kf in (("historical", lambda x: x.get("url") or x["name"]),
                        ("repository_checks", lambda x: json.dumps(x, sort_keys=True)),
                        ("mitre_attack_archived", lambda x: json.dumps(x, sort_keys=True))):
            if key in d:
                out[key], added = union(out.get(key, []), d[key], kf)
                changes += [f"+ {key}: {short(x)}" for x in added]
        log.append((ref, changes))
    out["entries"] = [by_id[i] for i in sorted(by_id)]
    out["reviewed_on"] = max(e["reviewed_on"] for e in out["entries"])
    (ROOT / "data" / "ecosystem.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"# Consolidação de data/ecosystem.json\n\nBase: `{base_ref}` · "
          f"resultado: **{len(out['entries'])} entradas**, revisão {out['reviewed_on']}\n")
    for ref, changes in log:
        print(f"## `{ref}`\n")
        print("\n".join(f"- {c}" for c in changes) if changes else "- nada que a base não tenha")
        print()
    print("## Revisão manual (mesma data, valores diferentes; mantido o da base)\n")
    print("\n".join(f"- {r}" for r in review) if review else "- nenhum")


if __name__ == "__main__":
    main()

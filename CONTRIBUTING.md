# 🤝 Contribuindo com o mapa

[← Início](README.md)

Inclua apenas recursos cuja relação com o escopo seja explicável: CTI, modelagem, detecção, defesa, emulação, resposta, resiliência, IA, OT ou automação de segurança.

## Fluxo em quatro passos

1. Edite **somente** `data/ecosystem.json` (e `data/trilha.json`, se mexer na trilha).
2. Rode `python3 scripts/build_catalog.py`. Ele valida o JSON e regenera `docs/catalogo.md`, `docs/trilha.md`, `data/ecosystem.csv`, `assets/ecosystem.js` e o bloco de números do README.
3. Abra `index.html` no navegador e confira a entrada nova.
4. Abra o PR. O workflow `validate` roda `build_catalog.py --check` e falha se algo estiver fora de sincronia.

## Campos de uma entrada (schema 2.0)

| Campo | Obrigatório | Valores |
|---|:-:|---|
| `id` | ✔ | `E` + 3 dígitos, sequencial; nunca reutilize |
| `name`, `url` | ✔ | URL primária com `https://` |
| `origin` | ✔ | texto livre com o mantenedor |
| `owner_type` | ✔ | `mitre`, `ctid`, `colaboracao`, `governanca-aberta`, `governo`, `padrao`, `comunidade`, `fornecedor`, `outro` |
| `layer` | ✔ | uma camada de `vocab.layer` (adversario, modelagem, telemetria, deteccao, defesa, engano, validacao, resposta, vulnerabilidade, cti, maturidade, dados, conformidade, padrao, formacao) |
| `domains` | ✔ | lista de `vocab.domains` |
| `purpose`, `output` | ✔ | para que usar e o que se entrega |
| `priority` | ✔ | `P1` ou `P2`, com justificativa no PR |
| `status` | ✔ | `ativo`, `baixa-atividade`, `parado`, `n/v` |
| `version` | | versão e data; indique "(tag)" ou "(PyPI)" quando vier dessas fontes |
| `formats`, `relations`, `notes`, `repo` | | `relations` só com IDs existentes |
| `archived`, `license_api`, `pushed_at` | | preenchidos por `scripts/check_repos.py` |
| `reviewed_on`, `verification` | ✔ | data e como foi verificado |

## Revisão

1. Verificar duplicação por nome, URL canônica e função.
2. Não classificar um projeto como MITRE só porque usa ATT&CK.
3. Distinguir framework, base de conhecimento, ferramenta, padrão, dataset e publicação.
4. Confirmar migrações e substituições na fonte; manter o histórico em `historical`.
5. Separar inferência editorial de afirmação do mantenedor.
6. Não inferir eficácia de um controle a partir de crosswalk ou de cobertura visual.
7. Não apresentar exemplos hipotéticos como resultados executados.
8. Não copiar material de terceiros sem revisar seus termos.

O catálogo não aceita "ranking top" baseado só em estrelas nem promessas de cobertura total sem evidência.

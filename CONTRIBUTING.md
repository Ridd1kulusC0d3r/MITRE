# 🤝 Contribuindo com o mapa

[← Início](README.md) · [Regras para agentes](CLAUDE.md)

Inclua apenas recursos cuja relação com o escopo seja explicável: CTI, modelagem, detecção, defesa, emulação, resposta, resiliência, IA, OT ou automação de segurança.

## Fluxo em quatro passos

1. Parta da `main` atualizada e crie uma branch.
2. Edite **só a fonte**, de preferência pela CLI, que valida e carimba a data de revisão:
   ```bash
   python3 -m atlas set E025 "version=v4.19.0 (tag)" "verification=Tag Git conferida em 12/11/2026"
   python3 -m atlas new name="Ferramenta" url=https://… origin="Mantenedor" owner_type=comunidade \
       layer=deteccao "domains=enterprise;cloud" purpose="…" output="…" priority=P2 status=ativo verification="…"
   ```
   Também vale editar `data/entries/E###.json` à mão. Trilha em `data/trilha.json`; cores e ícones em `design/tokens.json`.
3. Rode `python3 -m atlas check` e `python3 -m unittest`. Para ver o resultado sem sujar o repositório: `python3 -m atlas build --out dist` e abra `dist/…`, ou rode `python3 -m atlas build` e descarte os derivados antes do commit.
4. Abra o PR. O `validate` reprova PR que altere arquivo gerado (`python3 -m atlas generated` lista quais). Depois do merge, o `publish` regenera catálogo, CSV, JSON agregado, SVGs, explorador e os números do README.

## O que é fonte e o que é gerado

| Fonte (edite) | Gerado (não edite) |
|---|---|
| `data/entries/E###.json` · `data/vocab.json` · `data/historical.json` · `data/meta.json` · `data/trilha.json` | `data/ecosystem.json` · `data/ecosystem.csv` · `docs/catalogo.md` · `docs/trilha.md` |
| `design/tokens.json` | `assets/tokens.css` · `assets/*.svg` · `assets/ecosystem.js` |
| `index.html` · `site/` · README fora dos marcadores | blocos `<!-- nome:start/end -->` do README |

## Campos de uma entrada

| Campo | Obrigatório | Valores |
|---|:-:|---|
| `id` | ✔ | `E` + 3 dígitos, sequencial (`atlas new` escolhe); nunca reutilize |
| `name`, `url` | ✔ | URL primária com `https://` |
| `origin` | ✔ | texto livre com o mantenedor |
| `owner_type` | ✔ | `mitre`, `ctid`, `colaboracao`, `governanca-aberta`, `governo`, `padrao`, `comunidade`, `fornecedor`, `outro` |
| `layer` | ✔ | uma camada de `vocab.layer` (adversario, modelagem, telemetria, deteccao, defesa, engano, validacao, resposta, vulnerabilidade, cti, maturidade, dados, conformidade, padrao, formacao) |
| `domains` | ✔ | lista de `vocab.domains` |
| `purpose`, `output` | ✔ | para que usar e o que se entrega |
| `priority` | ✔ | `P1` ou `P2`, com justificativa no PR |
| `status` | ✔ | `ativo`, `baixa-atividade`, `parado`, `n/v` |
| `version` | | versão e data; indique "(tag)" ou "(PyPI)" quando vier dessas fontes |
| `formats`, `relations`, `notes`, `repo`, `legacy_category` | | `relations` só com IDs existentes |
| `archived`, `license_api`, `pushed_at`, `latest_release` | | preenchidos por `scripts/check_repos.py --write` |
| `reviewed_on`, `verification` | ✔ | `AAAA-MM-DD` e como foi verificado |

Chave fora desta lista é erro de validação. Avisos (relação sem recíproca, entrada ativa sem versão) não bloqueiam.

## Revisão

1. Verificar duplicação por nome, URL canônica e função.
2. Não classificar um projeto como MITRE só porque usa ATT&CK.
3. Distinguir framework, base de conhecimento, ferramenta, padrão, dataset e publicação.
4. Confirmar migrações e substituições na fonte; manter o histórico em `historical`.
5. Separar inferência editorial de afirmação do mantenedor.
6. Não inferir eficácia de um controle a partir de crosswalk ou de cobertura visual.
7. Não apresentar exemplos hipotéticos como resultados executados.
8. Não copiar material de terceiros sem revisar seus termos.

## Identidade visual

Cores, ícones e textos de marca vivem em `design/tokens.json`. `tests/test_design.py` confere contraste WCAG AA, distância entre as cores das camadas (inclusive em deuteranopia) e que nenhum arquivo de `atlas/` ou `site/` tenha cor literal. Depois de mudar o layout de um SVG de forma intencional, atualize as referências dos testes com `ATLAS_UPDATE_GOLDEN=1 python3 -m unittest tests.test_atlas` e a imagem social com `node scripts/render_social.js`.

O catálogo não aceita "ranking top" baseado só em estrelas nem promessas de cobertura total sem evidência.

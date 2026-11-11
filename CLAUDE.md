# MITRE Ecosystem Atlas — regras para agentes

Catálogo curado do ecossistema MITRE/CTID em pt-BR. Python somente stdlib.

## Onde editar

| Quero mudar… | Edite | Nunca edite |
|---|---|---|
| uma entrada do catálogo | `data/entries/E###.json` via `python3 -m atlas set`/`new` | `data/ecosystem.json`, `data/ecosystem.csv`, `docs/catalogo.md`, `assets/*` |
| vocabulário, histórico, metadados | `data/vocab.json`, `data/historical.json`, `data/meta.json` | — |
| trilha | `data/trilha.json` | `docs/trilha.md` |
| cor, ícone, tipografia, textos de marca | `design/tokens.json` | literais de cor em `atlas/` ou `site/` |
| explorador | `index.html`, `site/app.css`, `site/app.js` | `assets/ecosystem.js`, `assets/tokens.css` |
| README | texto fora dos marcadores `<!-- nome:start/end -->` | o conteúdo entre marcadores |

`python3 -m atlas generated` lista os derivados. O workflow `publish` os regenera na `main`; o `validate` reprova PR que os altere.

## Comandos

```bash
python3 -m atlas check                      # valida a fonte (avisos não bloqueiam)
python3 -m atlas show E001
python3 -m atlas set E025 "version=v4.19.0 (tag)" "verification=Tag Git conferida em 12/11/2026"
python3 -m atlas new name=… url=https://… origin=… owner_type=… layer=… domains=a;b \
    purpose=… output=… priority=P2 status=ativo verification=…
python3 -m unittest                         # 29+ testes; rode antes de cada commit
python3 -m atlas build --out dist           # opcional: ver o resultado sem tocar no repositório
```

`set` e `new` carimbam `reviewed_on` com a data de hoje (America/Sao_Paulo) e desfazem a gravação se a validação falhar.

## Fluxo de trabalho

1. Comece **sempre** de `origin/main` atualizada: `git fetch origin main && git checkout -B <branch> origin/main`.
2. Se não houver nada novo e verificado, **não crie branch nem commit**. Diga que não houve mudança.
3. Uma execução = uma branch = um PR para a `main`, pequeno (só `data/entries/` e, se couber, um documento em `docs/`).
4. Antes do commit: `python3 -m atlas check` sem erros e `python3 -m unittest` verde.
5. Não deixe branch sem PR. Branch sem PR é trabalho perdido: a próxima execução parte da `main` e refaz tudo.

## Regras de conteúdo

- Versão só entra se conferida na fonte (release, tag Git, PyPI, bundle). Escreva em `verification` o que foi lido e quando.
- Não classifique como MITRE um projeto só porque usa ATT&CK. Não infira eficácia de cobertura visual.
- Relação (`relations`) só com IDs existentes; IDs nunca são reaproveitados.
- Datas: `AAAA-MM-DD` nos dados, `dd/mm/aaaa` no texto.
- Novidade relevante para quem usa o catálogo vai também em `docs/historico-e-manutencao.md`, seção "Registro de revisões incrementais".

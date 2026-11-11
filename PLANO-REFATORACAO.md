# Plano de refatoração — MITRE Ecosystem Atlas

Plano para execução pelo Opus (`claude-opus-5-5`), uma fase por sessão e por PR.
Escrito em 11/11/2026 a partir do estado real do repositório. Apague este arquivo no PR da Fase 5.

## 1. Diagnóstico (medido, não suposto)

| # | Problema | Evidência |
|---|---|---|
| D1 | O trabalho diário nunca chega à `main` | `main` parada em `e9bf50d` (30/10). Dez branches `claude/blissful-bohr-*` com 1 commit cada, todas partindo da `main`, nenhuma com PR. |
| D2 | A rotina diária refaz o mesmo trabalho | Workbench 4.18.0 foi "descoberto" em 04/11, 05/11 e 10/11; ATT&CK v20.1 em 06/11, 08/11 e 11/11. Cada sessão começa da `main` velha. |
| D3 | As branches são inconciliáveis por `git merge` | Todas editam `data/ecosystem.json` (4.031 linhas, um arquivo) e `assets/ecosystem.js` (114 KB em **uma linha**). `E130` tem nomes diferentes em `v7b1yh` e `iqcvfs`. |
| D4 | O CI falha por desenho | `validate` compara byte a byte 7 arquivos gerados e versionados. Quem edita o JSON e esquece o gerador quebra o build (runs #8 e #9). |
| D5 | Metadado global editado à mão | `reviewed_on` continua `2026-10-23` em 5 branches cujos commits dizem "revisão 04/11", "05/11", "10/11". Selo "revisão 22/10/2026" fixo no README. |
| D6 | `scripts/build_catalog.py` é um monólito | 376 linhas: validação, 6 renderizadores, paleta, tipografia e layout de SVG no mesmo arquivo. Sem testes. |
| D7 | Identidade visual duplicada e implícita | Cores das camadas definidas em `build_catalog.py` (`LAYER_COLOR`) **e** em `index.html` (`COLOR`). Tokens de tema só no HTML. Emojis fazem o papel de ícones e variam por sistema operacional. |
| D8 | `monitor.yml` só relata | Detecta versão nova do ATT&CK e escreve no resumo da execução, que ninguém lê. Roda uma vez por mês. |
| D9 | Actions desatualizadas | `actions/checkout@v4` e `actions/setup-python@v5` rodam em Node 20, já depreciado (aviso no log). |
| D10 | A rotina agendada não tem contrato | Tarefa "MITRE" (diária, 02:35 America/Sao_Paulo), prompt de três linhas: "procurar novas ferramentas e frameworks do MITRE … Incluir atualizado". Não diz onde gravar, como validar nem como integrar. |

Causa raiz: **dados, arquivos derivados e apresentação vivem no mesmo commit, e não existe caminho de integração.**
D1, D2 e D10 são de processo; D3, D4 e D5 são de arquitetura de dados; D6 e D7 são de código.

## 2. Arquitetura alvo

```
data/
  entries/E001.json … E134.json   # FONTE: um arquivo por entrada (fim dos conflitos)
  vocab.json                      # FONTE: camadas, domínios, status, prioridade, origem
  historical.json                 # FONTE: itens históricos e depreciados
  meta.json                       # FONTE: escopo, limites de verificação, attack_release
  trilha.json                     # FONTE (inalterado)
  repository_checks.json          # escrito só por máquina (check_repos)
design/
  tokens.json                     # FONTE ÚNICA da identidade: cores, tipografia, raios, espaços
  icons/*.svg                     # um ícone por camada + marca
atlas/                            # pacote Python, somente stdlib
  model.py                        # carga, validação, agregados derivados (reviewed_on = máx. das entradas)
  theme.py                        # lê design/tokens.json; emite variáveis CSS e constantes SVG
  render/catalog.py csv.py trilha.py bundle.py readme.py banner.py layer_map.py site.py
  cli.py                          # python3 -m atlas <check|build|new|set|merge-legacy>
tests/                            # unittest: validação, renderizadores, golden files
site/                             # modelos: index.html, app.js, app.css (sem dados embutidos)
scripts/                          # ferramentas de análise (attack_diff, xwalks…) — ficam como estão
dist/                             # saída do build, no .gitignore
```

Regras que a arquitetura impõe:

1. **Fonte e derivado não se misturam.** Uma branch de conteúdo toca só `data/` e `docs/` escritos à mão.
   Derivados (`docs/catalogo.md`, `docs/trilha.md`, `data/ecosystem.json`, `data/ecosystem.csv`,
   `assets/*.svg`, `assets/ecosystem.js`, bloco de números do README) são escritos **somente** pelo
   workflow `publish` na `main`.
2. **`check` valida a fonte, não bytes de derivados.** O CI de PR roda `python3 -m atlas check`,
   os testes e um `build` em `dist/`. Não existe mais "arquivo desatualizado".
3. **Nada global é digitado.** `reviewed_on` do catálogo, contagens, selos de versão do README e os
   chips do banner são calculados a partir das entradas.
4. **Uma definição de identidade.** HTML, SVGs e README leem `design/tokens.json` via `atlas/theme.py`.
5. **Compatibilidade.** `data/ecosystem.json` continua existindo no mesmo caminho e schema 2.0 (agora gerado),
   porque `scripts/*.py`, `monitor.yml` e links externos dependem dele.

## 3. Decisões que dependem do dono do repositório

Cada uma tem padrão recomendado; o Opus segue o padrão se não houver resposta, e registra no PR.

| # | Decisão | Padrão recomendado |
|---|---|---|
| Q1 | Publicar o explorador no GitHub Pages? | Sim, via Actions (`dist/` como artefato). Precisa ativar Pages → Source: GitHub Actions nas configurações. |
| Q2 | Deixar o workflow `publish` fazer commit dos derivados na `main`? | Sim, com `permissions: contents: write` e `[skip ci]`. Se a `main` tiver proteção de branch, usar PR automático. |
| Q3 | Apagar as 11 branches `claude/blissful-bohr-*` depois da consolidação? | Sim, só depois do PR da Fase 0 mesclado. **Pedir confirmação explícita antes de apagar.** |
| Q4 | Direção da identidade visual (seção 5) | Evolução da atual (azul-noite + verde-água), não ruptura. |
| Q5 | Nome "MITRE Ecosystem Atlas" | Manter, com o aviso de independência visível. Nunca imitar marca, logotipo ou tipografia da MITRE. |

## 4. Fases

Cada fase: branch própria a partir da `main` atualizada, um PR, critérios de aceite verificáveis.
Não iniciar uma fase com o PR da anterior aberto.

### Fase 0 — Consolidar o trabalho perdido (desbloqueia tudo)

Objetivo: levar para a `main` o conteúdo válido das dez branches, sem `git merge`.

1. Base: `claude/blissful-bohr-iqcvfs` (11/11, 131 entradas, E001–E134; é a mais completa).
2. Escrever `scripts/merge_legacy.py` (descartável): para cada branch, ler `data/ecosystem.json` com
   `git show <ref>:data/ecosystem.json` e comparar **por `id`** com a base. Relatar, campo a campo,
   o que a branch tem e a base não. Regra de resolução: vence o valor com `reviewed_on` mais recente;
   empate ou campo de texto divergente vai para uma lista de revisão manual.
   Conflito conhecido: `E130` ("Caldera MCP (plugin LLM)" em `v7b1yh` × "Caldera MCP (plugin)" em `iqcvfs`).
3. Documentos escritos à mão, revisão manual com diff de três vias contra a `main`:
   - `docs/historico-e-manutencao.md` — `5t5uu9`, `o7znzs`, `n7i227`, `j8ts7k`, `iqcvfs`
   - `docs/novidades-2026.md` — `o7znzs`, `40jkhp`, `n5cpme`, `iqcvfs`
   - `docs/novas-referencias-2026-11-09.md` (só em `v7b1yh`) e `-2026-11-11.md` (só em `iqcvfs`)
   - `README.md` — `n7i227`, `v7b1yh`, `iqcvfs`
   - `scripts/*` alterados em `iqcvfs` — conferir que são correções e não regressões
4. Corrigir `reviewed_on` global para a maior data entre as entradas.
5. Rodar `python3 scripts/build_catalog.py` e depois todos os passos de `validate.yml`.

Aceite: `build_catalog.py --check` passa; nenhuma entrada, nota ou linha de histórico presente em qualquer
branch ficou de fora (anexar a saída do `merge_legacy.py` ao PR); pelo menos as 131 entradas da base,
com os IDs já publicados preservados (as lacunas de numeração existentes não são reaproveitadas).
Depois de mesclado: Q3.

### Fase 1 — Separar dados, extrair o pacote, cobrir com testes

Princípio: **mudança de estrutura sem mudança de saída.** A identidade visual não é tocada aqui.

1. Antes de mexer: salvar a saída atual dos 7 derivados em `tests/golden/`.
2. Criar `atlas/` movendo o código de `build_catalog.py` função por função (`validate` → `model.py`;
   `render_*` → `render/`; `LAYER_COLOR`, `FONT`, `MONO` → `theme.py` lendo `design/tokens.json` com os
   **mesmos valores de hoje**).
3. `python3 -m atlas split`: quebrar `data/ecosystem.json` em `data/entries/E###.json` + `vocab.json` +
   `historical.json` + `meta.json` + `repository_checks.json`. Chaves em ordem estável, indentação 2,
   UTF-8 sem escape, quebra de linha final.
4. `model.py` remonta o agregado em memória; `render/bundle.py` gera `data/ecosystem.json` idêntico ao schema 2.0.
5. Validações novas em `model.py`: `reviewed_on` e datas em ISO 8601; nome do arquivo igual ao `id`;
   URL duplicada; relação não recíproca vira aviso; chave desconhecida vira erro; `version` obrigatória
   para `status: ativo` (aviso). Mensagem de erro sempre com o caminho do arquivo.
6. CLI: `check`, `build [--out dist]`, `new` (cria a próxima entrada com o próximo ID livre e campos
   obrigatórios), `set E### campo=valor` (atualiza e carimba `reviewed_on` com a data de hoje em
   America/Sao_Paulo). `new` e `set` são a interface da rotina diária.
7. `scripts/build_catalog.py` vira um atalho de 5 linhas que chama `atlas.cli` (compatibilidade).
8. `tests/` com `unittest`: uma falha por regra de validação; golden dos 7 derivados; `split` seguido de
   `bundle` devolve o JSON original; `fit()` e `xml()`.

Aceite: `python3 -m unittest` passa; os 7 derivados saem **byte a byte iguais** aos de antes (exceto a
ordem de chaves do JSON agregado, se documentada); nenhuma dependência fora da stdlib; `scripts/*.py`
continuam funcionando sem alteração.

### Fase 2 — CI, publicação e monitoramento

1. `validate.yml` (PR e push em qualquer branch): `atlas check`, `unittest`, `atlas build --out dist`,
   `py_compile`, `bash -n`, JSON de `layers/`. Falha se o PR alterar um arquivo derivado à mão
   (lista em `atlas/render/__init__.py`), com mensagem dizendo o que fazer.
2. `publish.yml` (push na `main`): `atlas build`, grava os derivados versionados, faz commit
   `chore(build): regenera derivados [skip ci]` se houver diferença, e publica `dist/` no Pages (Q1, Q2).
   `concurrency` para não haver duas publicações simultâneas.
3. `monitor.yml`: semanal em vez de mensal; quando houver versão nova do ATT&CK ou repositório arquivado,
   **abre ou atualiza uma issue** com rótulo `monitor` em vez de só escrever no resumo. `permissions: issues: write`.
4. Atualizar as actions para as versões atuais em Node 24 (conferir a versão vigente na fonte antes de fixar).
5. `.gitattributes`: derivados marcados `linguist-generated=true` (somem dos diffs de PR).
6. `.github/pull_request_template.md` curto: o que mudou, fonte verificada, `atlas check` passou.

Aceite: um PR que muda só `data/entries/E001.json` passa sem tocar em derivado; ao mesclar, a `main`
recebe o commit de build e o Pages mostra a mudança; um PR que edita `docs/catalogo.md` à mão falha
com mensagem clara.

### Fase 3 — Identidade visual

Ver seção 5 para a especificação. Passos:

1. `design/tokens.json` com tema claro e escuro; `atlas/theme.py` emite `site/tokens.css`
   (variáveis CSS) e as constantes usadas pelos SVGs. Remover `COLOR` de `index.html` e os hexadecimais
   soltos de `render/banner.py` e `render/layer_map.py`.
2. Marca: `design/icons/mark.svg` e derivados (`favicon.svg`, ícone 512 px).
3. Ícones de camada (15) em SVG de traço único, `currentColor`, grade 24 px. Substituem os emojis no
   explorador e nos SVGs. No Markdown do GitHub os emojis permanecem (SVG embutido não é renderizado em tabelas).
4. Redesenhar `render/banner.py` e `render/layer_map.py` sobre os tokens. Gerar **duas** variantes
   (clara e escura) e usar `<picture>` com `prefers-color-scheme` no README.
5. Separar `index.html` em `site/index.html` + `site/app.css` + `site/app.js`. Os dados continuam em
   `assets/ecosystem.js` via `<script>` para funcionar com `file://`.
6. Explorador: aplicar a especificação; estado dos filtros na URL (`#explorar?camada=deteccao&q=sigma`);
   foco visível; navegação por teclado nas abas; `prefers-reduced-motion`.
7. Imagem de pré-visualização social 1280×640 (`assets/social.png`), gerada com o Chromium do
   ambiente a partir de um SVG do build e versionada (o GitHub não aceita SVG nesse campo).
8. README: selos de versão gerados pelo build (fim do "revisão 22/10/2026" fixo).

Verificação obrigatória (Playwright, já instalado): capturas do explorador em 1440 px e 390 px, tema
claro e escuro, nas quatro abas; conferir sem rolagem horizontal, contraste de texto ≥ 4,5:1, e
distinção das 15 camadas em simulação de deuteranopia. Anexar as capturas ao PR.

Aceite: nenhum hexadecimal de cor fora de `design/tokens.json` (teste automatizado com `grep`);
as capturas anexadas; `atlas build` determinístico (duas execuções, mesma saída).

### Fase 4 — Contrato da rotina diária

1. `CLAUDE.md` na raiz (lido por toda sessão): editar só `data/entries/`; usar `atlas new`/`atlas set`;
   nunca editar derivados; rodar `atlas check` e `unittest` antes do commit; **começar de
   `origin/main` atualizada**; abrir PR para a `main` e não deixar branch órfã; um PR por execução;
   se não houver novidade, não criar branch nem commit.
2. Reescrever o prompt da tarefa agendada "MITRE" (hoje três linhas) com: fontes a consultar, regra de
   verificação na fonte, comando para registrar cada achado, critério de "nada novo", e entrega por PR
   com mesclagem automática quando o `validate` passar. **A alteração da tarefa agendada só é feita
   com confirmação do dono**; o Opus entrega o texto pronto no PR.
3. Ativar mesclagem automática no repositório (configuração manual do dono) ou, sem ela, a rotina
   mescla o próprio PR depois do `validate` verde.

Aceite: uma execução manual da rotina produz um PR pequeno (só `data/entries/` e, se couber, um doc),
com `validate` verde, sem derivados no diff.

### Fase 5 — Documentação e limpeza

Atualizar `CONTRIBUTING.md`, `docs/historico-e-manutencao.md` e o README para o fluxo novo; registrar a
migração de schema (2.0 → 2.1: fonte fragmentada, agregado gerado); remover `scripts/merge_legacy.py` e
este arquivo.

## 5. Especificação da identidade visual

Direção: **atlas técnico** — cartografia de ameaças, não "painel hacker". Sóbrio, legível, imprimível.

- **Marca.** Símbolo: grade 3×3 de células arredondadas com uma diagonal acesa (a matriz ATT&CK lida
  como rota do adversário à resposta). Funciona em 16 px e em uma cor. Não usar escudo, cadeado,
  caveira nem qualquer elemento da marca MITRE.
- **Cores de base.** Noite `#0b1020`, painel `#121a2e`, linha `#263250`, texto `#e6edf3`, apagado
  `#9aa7bd`, destaque `#7ee0d6` (verde-água). Tema claro: fundo `#f6f8fa`, texto `#1f2328`, destaque
  `#0b7a70` (o verde-água claro não tem contraste sobre branco). São os valores atuais, agora nomeados.
- **Cores das 15 camadas.** Manter a lógica atual (fluxo principal em sequência quente → fria; fundação
  em neutros), mas **validar e ajustar**: hoje `dados` `#6e7681`, `conformidade` `#768390` e `padrao`
  `#636e7b` são praticamente indistinguíveis. Cada camada recebe cor + ícone, nunca só cor.
- **Tipografia.** Pilha do sistema (sem fonte remota: o explorador precisa abrir offline). Sans para
  texto, mono para IDs (`E001`, `T1562`), versões e comandos. Escala: 12 / 13 / 15 / 20 / 26 / 40.
- **Forma.** Raio 6 (selos), 12 (cartões), 18 (painéis). Borda de 1 px; sombra só no tema claro.
  Faixa de cor da camada à esquerda do cartão, como hoje.
- **Voz.** Português direto, sem superlativo. Rótulo diz o que o item faz. Sempre visível:
  "independente, sem afiliação ou endosso da MITRE".
- **Aplicações.** Banner do README (claro e escuro), mapa de camadas, favicon, imagem social,
  explorador, selos. Todas geradas pelo build a partir dos tokens.

## 6. Riscos

| Risco | Mitigação |
|---|---|
| Perder conteúdo na consolidação | Fase 0 por comparação de entradas, com relatório anexado; branches só são apagadas depois, com confirmação. |
| Quebrar quem consome `data/ecosystem.json` | Caminho e schema mantidos; teste de ida e volta na Fase 1. |
| `publish` em laço de commits | `[skip ci]` + só faz commit se houver diferença + `concurrency`. |
| A rotina diária rodar no meio da migração | Pausar a tarefa "MITRE" da Fase 0 até a Fase 4 (decisão do dono). Sem pausa, cada execução cria mais uma branch a consolidar. |
| Refatoração e redesenho no mesmo PR | Proibido: Fase 1 exige saída idêntica; o visual só muda na Fase 3. |

## 7. Como executar

Uma sessão por fase, com o modelo `claude-opus-5-5`, e este pedido:

> Leia `PLANO-REFATORACAO.md` e execute **somente a Fase N**. Parta de `origin/main` atualizada,
> trabalhe em uma branch nova, cumpra todos os critérios de aceite, rode as verificações e abra um PR
> para a `main` descrevendo o que foi feito, o que foi verificado e o que ficou pendente. Não avance
> para a fase seguinte. Onde o plano pede confirmação do dono, pare e pergunte.

Ordem: 0 → 1 → 2 → 3 → 4 → 5. As fases 2 e 3 podem trocar de lugar; as demais não.

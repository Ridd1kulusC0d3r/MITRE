# 🗄️ Histórico, fontes e manutenção

[← Início](../README.md) · [Catálogo](catalogo.md) · [Novidades 2026](novidades-2026.md)

## Método e limites

Revisão em **22/10/2026**, com atualização incremental em **23/10/2026** (UTC), data local de São Paulo. Timestamps da API estão em UTC e podem aparecer como 23/10/2026. **Atualização de 11/11/2026:** ATT&CK v20.1, ATLAS 2026.10, versões de ferramentas e cinco entradas novas (E130–E134); só os itens tocados tiveram `reviewed_on` alterado.

1. Consultar portais oficiais MITRE, ATT&CK, CTID e fontes dos mantenedores.
2. Confirmar identidade e finalidade antes de classificar como MITRE, CTID ou externo.
3. **Conferir versões na fonte quando possível:** contagens do ATT&CK no bundle STIX, changelogs de D3FEND e ATLAS, tags Git e versões no PyPI. Essas entradas trazem `verification: "Verificado na fonte…"` no JSON.
4. Para o resto, usar pesquisa web e marcar o campo `status` como `n/v` quando não houver confirmação.
5. Separar referências históricas e registrar migrações declaradas pelo mantenedor.
6. Selecionar P1/P2 por utilidade ao fluxo de CTI, modelagem, detecção, defesa e resposta.

**Ferramentas de terceiros não foram instaladas nem avaliadas.** Os scripts deste repositório foram executados contra dados reais (ATT&CK 20.0, CAPEC 3.9, SigmaHQ e Atomic Red Team em 22/10/2026); o `d3fend_xwalk.py` foi testado apenas com dados sintéticos, porque o site do D3FEND não estava acessível do ambiente de teste.

Sinais e seus limites:

| Campo | Significa | Não significa |
|---|---|---|
| `archived=false` | o GitHub não marcou como arquivado | manutenção ativa |
| `pushed_at` | último push no repositório | último release ou mudança substantiva |
| `version` com "(tag)" | existe uma tag Git com esse nome | release estável |
| `license_api: NOASSERTION` | a API não reconheceu a licença | domínio público |
| `status: n/v` | não verificado nesta revisão | inativo |

## Repositórios arquivados

| Repositório | Estado | Orientação |
|---|---|---|
| [attack-control-framework-mappings](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings) | Arquivado | Mapeamentos NIST migraram para o Mappings Explorer. |
| [security-stack-mappings](https://github.com/center-for-threat-informed-defense/security-stack-mappings) | Arquivado | Mapeamentos de stacks migraram para o Mappings Explorer. |
| [attack_to_cve](https://github.com/center-for-threat-informed-defense/attack_to_cve) | Arquivado | Mapeamentos CVE migraram para o Mappings Explorer. |
| [caldera_pathfinder](https://github.com/center-for-threat-informed-defense/caldera_pathfinder) | Arquivado | Plugin histórico; não instalar como componente atual sem revisão. |
| [attack_to_veris](https://github.com/center-for-threat-informed-defense/attack_to_veris) | Arquivado | Mapeamentos VERIS migraram para o Mappings Explorer. |
| [m3tid](https://github.com/center-for-threat-informed-defense/m3tid) | Arquivado | Use o INFORM; não assuma equivalência de scores. |
| [attack-workbench-collection-manager](https://github.com/center-for-threat-informed-defense/attack-workbench-collection-manager) | Arquivado | Consulte a arquitetura atual do Workbench. |
| [pyattck](https://github.com/swimlane/pyattck) | Arquivado (17/03/2026) | Último release 7.1.2 em 2023. Use mitreattack-python ou attackcti. |
| [mitre-attack/attack-scripts](https://github.com/mitre-attack/attack-scripts) | Arquivado (dez/2023) | Use mitreattack-python. |
| [mitre-attack/evals_caldera](https://github.com/mitre-attack/evals_caldera) | Arquivado (set/2023) | Plugin da rodada 1 das Evaluations; histórico. |
| [mitre-attack/joystick](https://github.com/mitre-attack/joystick) | Arquivado (set/2023) | Use evals.mitre.org. |
| [mitre-attack/attack-datasources](https://github.com/mitre-attack/attack-datasources) | Arquivado (set/2023) | Modelo de Data Sources substituído na v18. |
| [mitre-attack/attack-datasources-stix-beta](https://github.com/mitre-attack/attack-datasources-stix-beta) | Arquivado (set/2023) | Idem; só para estudo histórico. |
| [mitre-attack/tram](https://github.com/mitre-attack/tram) | Arquivado (out/2021) | Versão antiga; a atual está no CTID. |
| [mitre-attack/attack-evals](https://github.com/mitre-attack/attack-evals) | Arquivado (abr/2021) | Site antigo; use evals.mitre.org. |
| [mitre-attack/attack-archives](https://github.com/mitre-attack/attack-archives) | Arquivado (jul/2020) | Use Version History do site. |

## Projetos, objetos e arquivos depreciados

| Item | O que aconteceu | Use no lugar |
|---|---|---|
| MITRE Shield | aposentado em 18/10/2021 | Engage |
| PRE-ATT&CK | absorvido na v8 (out/2020) | táticas TA0043 Reconnaissance e TA0042 Resource Development |
| ATT&CK Data Sources (objeto) | removidos na v18 (out/2025) | Data Components ligados a Analytics e Detection Strategies |
| Defense Evasion (nome) | dividida na v19 (28/04/2026) | TA0005 Stealth + TA0112 Defense Impairment |
| T1562 Impair Defenses e subtécnicas | revogadas na v19 | T1685, T1686, T1688–T1690 ([tabela](novidades-2026.md#-as-17-técnicas-que-saíram-entre-v181-e-v200)) |
| `dist/ATLAS.yaml` | depreciado | `dist/v6/ATLAS-<versão>.yaml` |
| CALDERA em `mitre/caldera` | doado à ASF | Apache Caldera, `apache/caldera` |

## Atenção adicional

- **RE&CT:** não arquivado, mas sem push desde 31/05/2022. Útil como taxonomia; revise antes de automatizar resposta.
- **Atomic Threat Coverage:** sem atualização desde 2022.
- **CAR:** sem atualização relevante desde mai/2025; as Detection Strategies do ATT&CK ocupam esse papel.
- **Security Datasets:** último push em 20/03/2024; avalie representatividade.
- **Cloud Analytics:** último push em 25/04/2023; adapte aos esquemas atuais.
- **attack-arsenal** (2021) e **caret** (2020): parados e mantidos no catálogo como referência. Sobre o arquivamento do attack-arsenal as consultas divergem: a checagem de 23/10/2026 (campo `mitre_attack_archived` do JSON) o lista como *Public archive*, a listagem da organização lida em 22/10/2026 não. Confirme na página do repositório.
- **Atividade na org mitre-attack (out/2026):** workbench-frontend e rest-api (22/10), website e navigator (20/10), taxii-server e deployment (16/10), mitreattack-python e attack-stix-data (13/10). Menos ativos: attack-data-model (25/06/2026), car (16/05/2025), bzar (26/06/2024).
- **Organização mitre-attack em 11/11/2026:** 21 repositórios, nenhum novo desde a revisão anterior. Atividade recente: attack-data-model, workbench-rest-api e workbench-frontend (09/11), website, mitreattack-python e attack-stix-data (05/11), navigator (04/11). O attack-arsenal aparece sem a marca *Public archive* na listagem da organização lida nesta data.
- **ATT&CK v20.1 (05/11/2026):** correção de dados; diff de técnicas vazio contra a v20.0 nos três domínios (medido com `attack_diff.py`).
- **ATLAS Agent:** dados embutidos da v2026.7, anteriores às renomeações da 2026.10.
- **atlas-navigator-data:** o README declara o projeto depreciado; STIX e camadas saem do atlas-data.
- **Engage:** tag v1.0 e pouca atividade; o método segue válido.
- **Mappings Editor:** beta público.
- **DeTT&CT:** 2.2.0 suporta o modelo da v18; suporte a v19/v20 não declarado.
- **D3FEND 1.6.0:** issue #709 relata mapeamentos para técnicas revogadas na v19.
- **CAPEC 3.9:** 15 mapeamentos para técnicas revogadas na v20 (medido nesta revisão).

## Fontes de descoberta e conferência

- [MITRE — Threat-Informed Defense](https://www.mitre.org/focus-areas/cybersecurity/threat-informed-defense)
- [MITRE — Capabilities & Resources](https://www.mitre.org/focus-areas/cybersecurity/capabilities-resources)
- [CTID — Our Work](https://ctid.mitre.org/projects/)
- [ATT&CK — Updates](https://attack.mitre.org/resources/updates/) · [Data & Tools](https://attack.mitre.org/resources/attack-data-and-tools/)
- [attack-stix-data — index.json](https://github.com/mitre-attack/attack-stix-data)
- [D3FEND — CHANGELOG](https://github.com/d3fend/d3fend-ontology/blob/master/CHANGELOG.md) · [FAQ](https://d3fend.mitre.org/faq/)
- [ATLAS Data — CHANGELOG](https://github.com/mitre-atlas/atlas-data)
- [SAF — portal](https://saf.mitre.org/)
- [OASIS CTI — STIX/TAXII](https://oasis-open.github.io/cti-documentation/faq.html)
- [FIRST — padrões](https://www.first.org/standards/)
- [NIST — SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

## Rotina de atualização

| O quê | Como | Quando |
|---|---|---|
| Validação da fonte | workflow `validate`: `python3 -m atlas check`, testes e build de fumaça; reprova PR que edite derivados | a cada push e PR |
| Derivados e site | workflow `publish`: `python3 -m atlas build`, commit dos derivados e GitHub Pages | a cada merge na `main` |
| Sinais de manutenção e versão do ATT&CK | workflow `monitor` (`scripts/monitor.py`): relatório e issue `monitor` aberta, atualizada ou fechada | semanal (segunda) e manual |
| Novidades do ecossistema | tarefa agendada com o prompt de [rotina-diaria.md](rotina-diaria.md): um PR por execução, nada quando não há novidade | diária |
| Conteúdo | revisar redirecionamentos, releases, licenças e novos projetos CTID | a cada release do ATT&CK (abril e outubro) |

`python3 -m atlas set` carimba `reviewed_on` só na entrada alterada; a data global do catálogo é a maior entre as entradas. Preserve entradas históricas com motivo e alternativa.

## Proveniência e licenças

Curadoria independente com resumos e scripts próprios. Os arquivos em `crosswalks/` e `layers/` são **derivados** de dados da MITRE (ATT&CK, CAPEC), do SigmaHQ e do Atomic Red Team, gerados pelos scripts deste repositório; os termos de uso das fontes continuam valendo. Links não transferem direitos. Marcas MITRE, ATT&CK, D3FEND, ATLAS e demais pertencem aos respectivos titulares.

## Registro de revisões incrementais

Revisões diárias feitas em branches que não chegaram a ser mescladas e foram consolidadas em 11/11/2026. Cada bloco descreve o que se sabia **naquela data**; o estado atual está no catálogo.

### Inventário da organização mitre-attack — 03/11/2026

Conferido na [lista de repositórios](https://github.com/orgs/mitre-attack/repositories) e em [attack.mitre.org/resources/updates](https://attack.mitre.org/resources/updates/): **21 repositórios, nenhum novo desde a revisão de 22/10/2026**. ATT&CK continua em **v20** (13/10/2026) e `mitreattack-python` em **6.3.1** (PyPI). Datas abaixo vêm da listagem pública (sem hora) e **não** substituem os `pushed_at` do catálogo; rode `check_repos.py` com token para atualizá-los.

| Repositório | Último push (listagem) | No catálogo |
|---|---|---|
| attack-navigator | 01/11/2026 | E024 (catálogo: 20/10) |
| attack-website | 30/10/2026 | E075 |
| attack-workbench-frontend | 25/10/2026 | E025 |
| attack-workbench-rest-api | 22/10/2026 | E073 |
| attack-workbench-taxii-server · -deployment | 16/10/2026 | E030 · E074 |
| mitreattack-python · attack-stix-data | 13/10/2026 | E028 · E026 |
| attack-data-model | 25/06/2026 | E029 |
| car | 16/05/2025 | E011 (site; repositório sem entrada própria) |
| bzar · attack-arsenal · caret | 2024 · 2021 · 2020 | E012 · E108 · E109 |
| attack-scripts, evals_caldera, joystick, attack-datasources, attack-datasources-stix-beta, tram, attack-evals, attack-archives | arquivados (2020–2023) | só `attack-scripts` citado acima; os demais sem entrada, por serem históricos |

Novidade de conteúdo na v20: campanhas sobre ataques a utilidades de água dos EUA e uma intrusão assistida por IA contra infraestrutura do governo mexicano; técnicas de IA em Enterprise e de execução/C2 em ICS; retorno da técnica Mobile *Deliver Malicious Application via Other Means*; totais de 971 Software, 182 Groups e 61 Campaigns. Contagens não conferidas contra o bundle STIX nesta rodada.

### Revisão incremental — 04/11/2026

Varredura de `attack.mitre.org` e das organizações `mitre-attack` e `center-for-threat-informed-defense`. Nenhuma ferramenta ou framework novo: ATT&CK v20.0 segue como versão atual e todos os repositórios das duas organizações já estão no catálogo. Atualizados apenas **Workbench v4.18.0** e **Workbench REST API v4.26.0** (pré-releases de 03/11/2026). Navigator (v5.3.2) e mitreattack-python (6.3.1) sem mudança.

### Revisão incremental — 06/11/2026

- **ATT&CK v20.1** publicado em 05/11/2026 (tag `v20.1` em `attack-stix-data`, junto com a retag de v20.0 na mesma data). Conteúdo detalhado não verificado: consulte o changelog em attack.mitre.org/resources/updates/. Contagens e tabelas deste repositório seguem baseadas na v20.0.
- **Nenhum repositório novo** nas organizações `mitre-attack` e `center-for-threat-informed-defense`: todos os 21 + 15 listados já estão no catálogo.
- **Atividade recente:** attack-website, mitreattack-python e attack-stix-data (05/11); attack-navigator e workbench-rest-api (04/11); workbench-frontend (03/11); CTID: fight-fraud-framework, technique-inference-engine, attack-sync e mappings-editor (05/11); attack-flow e top-attack-techniques (27/10).
- Navigator permanece em v5.3.2 (último release listado); versão do mitreattack-python não reverificada (PyPI inacessível).

### Atualização incremental — 08/11/2026

Conferência em attack.mitre.org, `attack-stix-data/index.json` e PyPI (a API do GitHub não estava acessível; a listagem de `github.com/orgs/mitre-attack/repositories` não pôde ser lida, então **novos repositórios da organização não foram verificados**).

| Item | Antes | Agora |
|---|---|---|
| ATT&CK (Enterprise, Mobile, ICS) | v20.0 · 13/10/2026 | **v20.1 · 05/11/2026** (correções de dados; v20.0 segue como versão maior) |
| attack-stix-data | v20.0 | v20.1 (bundles de 05/11/2026) |
| mitreattack-python | 6.3.1 | 6.3.2 e **6.4.0** (PyPI, 05/11/2026) |
| Contagem v20 (site) | — | Enterprise: 15 táticas, 227 técnicas, 479 subtécnicas, 703 Detection Strategies, 1770 Analytics |

### Atualização — 09/11/2026

Quatro ferramentas da organização `mitre` (Caldera MCP, Caldera for OT, Hipcheck, Grid Watch): [novas referências de 09/11/2026](novas-referencias-2026-11-09.md). Viraram as entradas E130–E133, revistas em 11/11.

### Atualização — 11/11/2026

ATT&CK v20.1, ATLAS 2026.10, versões de ferramentas e cinco entradas novas (E130–E134): [novas referências de 11/11/2026](novas-referencias-2026-11-11.md).

### Refatoração — 11/11/2026

Arquitetura refeita para acabar com as branches órfãs e com o CI vermelho por derivado desatualizado:
fonte fragmentada em `data/entries/` (um arquivo por entrada), pacote `atlas/` com CLI e testes,
derivados gerados só na `main` pelo workflow `publish`, identidade visual em `design/tokens.json`
e contrato para agentes em [CLAUDE.md](../CLAUDE.md). O agregado `data/ecosystem.json` continua no
mesmo caminho e no schema 2.0, agora gerado. Detalhes nos commits `fase-0` a `fase-5`.

### Revisão incremental — 12/11/2026

Varredura de `attack.mitre.org` e das organizações `mitre-attack` (21 repositórios) e `center-for-threat-informed-defense`. Nenhuma ferramenta ou framework novo; ATT&CK segue em v20.1 (tag de 05/11/2026). Única mudança: **Workbench REST API v4.26.1** (tag de 11/11/2026, atualização da dependência attack-data-model 4.12.0). Sem tag nova em Workbench frontend (v4.18.0), Navigator (v5.3.2), ATT&CK Data Model (v5.0.0-beta.3), TAXII Server (v2.0.1), attack-website (website-v4.4.1) e mitreattack-python (6.4.0 no PyPI). A segunda página da listagem do CTID (1 de 31 repositórios) não foi lida.

# 🗄️ Histórico, fontes e manutenção

[← Início](../README.md) · [Catálogo](catalogo.md) · [Novidades 2026](novidades-2026.md)

## Método e limites

Revisão em **22/10/2026**, com atualização incremental em **23/10/2026** (UTC), data local de São Paulo. Timestamps da API estão em UTC e podem aparecer como 23/10/2026.

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
| Validação do catálogo | workflow `validate` (`build_catalog.py --check`) | a cada push e PR |
| Sinais de manutenção | workflow `monitor` roda `check_repos.py` e publica o relatório no resumo do job | mensal (dia 1) e manual |
| Nova versão do ATT&CK | o mesmo workflow compara `index.json` com a versão registrada no catálogo | mensal e manual |
| Conteúdo | revisar redirecionamentos, releases, licenças e novos projetos CTID | a cada release do ATT&CK (abril e outubro) |

Atualize `reviewed_on` só nos itens efetivamente revisados. Preserve entradas históricas com motivo e alternativa.

## Proveniência e licenças

Curadoria independente com resumos e scripts próprios. Os arquivos em `crosswalks/` e `layers/` são **derivados** de dados da MITRE (ATT&CK, CAPEC), do SigmaHQ e do Atomic Red Team, gerados pelos scripts deste repositório; os termos de uso das fontes continuam valendo. Links não transferem direitos. Marcas MITRE, ATT&CK, D3FEND, ATLAS e demais pertencem aos respectivos titulares.

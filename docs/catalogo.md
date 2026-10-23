<!-- ARQUIVO GERADO por scripts/build_catalog.py a partir de data/ecosystem.json. Não edite à mão. -->

# 🗺️ Catálogo do ecossistema

[← Início](../README.md) · [Explorador interativo](../index.html) · [Crosswalks](crosswalks.md) · [Novidades 2026](novidades-2026.md) · [Histórico](historico-e-manutencao.md)

Revisão: **2026-10-23** · **126 entradas** (frameworks, ferramentas, dados, padrões e publicações). P1 = comece aqui; P2 = aprofunde por necessidade. Não é ranking de mercado.

**Legenda.** Origem: 🟦 MITRE oficial · 🟩 MITRE CTID · 🟪 Colaboração MITRE · 🟫 Fundação aberta (código MITRE doado) · ⬛ Governo · ⬜ Organismo de padrão · 🟨 Comunidade · 🟧 Fornecedor · ◻️ Outro  
Status: ✅ Ativo · ⏸️ Baixa atividade · 🧊 Parado · ❔ Não verificado

## Índice por camada

| Camada | Pergunta | Itens |
|---|---|:---:|
| 🎯 [adversario](#adversario) | O que o adversário faz | 15 |
| 🧭 [modelagem](#modelagem) | Como representar o cenário | 7 |
| 📡 [telemetria](#telemetria) | O que observar | 5 |
| 🔎 [deteccao](#deteccao) | Como detectar e avaliar | 16 |
| 🛡️ [defesa](#defesa) | Como reduzir exposição | 6 |
| 🎭 [engano](#engano) | Como enganar e engajar | 1 |
| 🧪 [validacao](#validacao) | Como validar | 16 |
| 🚑 [resposta](#resposta) | Como responder e investigar | 5 |
| 🩹 [vulnerabilidade](#vulnerabilidade) | Que fraquezas existem | 7 |
| 🕵️ [cti](#cti) | Como produzir e compartilhar CTI | 11 |
| 📈 [maturidade](#maturidade) | Como evoluir o programa | 2 |
| 🗄️ [dados](#dados) | Como consumir por código | 20 |
| ⚙️ [conformidade](#conformidade) | Como automatizar conformidade | 5 |
| 📐 [padrao](#padrao) | Padrões de base | 4 |
| 🎓 [formacao](#formacao) | Como aprender | 6 |

<a id="adversario"></a>
## 🎯 O que o adversário faz

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[ATLAS](https://atlas.mitre.org/)** `E004` | 🟦 MITRE | Modelar ameaças contra sistemas de IA e agentes: prompt injection, jailbreak, envenenamento de dados e abuso de ferramentas. | v2026.09 · 14/09/2026 | IA | P1 |
| ✅ | **[ATT&CK](https://attack.mitre.org/)** `E001` | 🟦 MITRE | Descrever comportamentos adversários observados; Enterprise, Mobile e ICS. | v20.0 · 13/10/2026 | Enterprise, Mobile, ICS/OT, IA | P1 |
| ✅ | **[ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)** `E115` | 🟦 MITRE | Comportamentos adversários contra sistemas de controle industrial. | v20.0 | ICS/OT | P1 |
| ✅ | **[AADAPT](https://aadapt.mitre.org/)** `E076` | 🟦 MITRE | Táticas e técnicas contra blockchain, ativos digitais e pagamentos com cripto. | lançado em 14/07/2025 | Ativos digitais, Fraude | P2 |
| ✅ | **[ATT&CK Mobile](https://attack.mitre.org/matrices/mobile/)** `E116` | 🟦 MITRE | Comportamentos adversários em Android e iOS. | v20.0 | Mobile | P2 |
| ✅ | **[CAPEC](https://capec.mitre.org/)** `E008` | 🟦 MITRE | Consultar padrões de ataque. | v3.9 | Enterprise | P2 |
| ❔ | **[CAVEaT](https://cloudsecurityalliance.org/artifacts/cloud-adversarial-vectors-exploits-and-threats)** `E023` | 🟪 CSA / colaboração MITRE | Estruturar ameaças e orientação de segurança para cloud. | — | Cloud | P2 |
| ✅ | **[DISARM](https://www.disarm.foundation/)** `E094` | 🟨 DISARM Foundation | Descrever táticas de manipulação e interferência informacional (FIMI). | v1.6.1 (tag) · v1.7 citada em mai/2026 | Desinformação | P2 |
| ✅ | **[ESTM](https://estm.mitre.org/)** `E006` | 🟦 MITRE | Explorar táticas e técnicas de ataques a sistemas embarcados. | ESTM 3.0 · jan/2026 | Embarcados | P2 |
| ❔ | **[FiGHT](https://fight.mitre.org/)** `E007` | 🟦 MITRE | Modelar ameaças ao ecossistema 5G. | — | 5G | P2 |
| ✅ | **[Fight Fraud Framework](https://github.com/center-for-threat-informed-defense/fight-fraud-framework)** `E045` | 🟩 MITRE / CTID | Estruturar análise comportamental de fraude financeira. | lançado em 09/04/2026 | Fraude | P2 |
| ✅ | **[Insider Threat TTP KB](https://github.com/center-for-threat-informed-defense/insider-threat-ttp-kb)** `E035` | 🟩 MITRE / CTID | Consultar comportamentos de ameaças internas. | — | Enterprise | P2 |
| ✅ | **[LOLBAS](https://lolbas-project.github.io/)** `E103` | 🟨 LOLBAS Project | Catálogo de binários nativos do Windows abusados por adversários, com técnicas ATT&CK. | — | Enterprise | P2 |
| ✅ | **[Secure AI (CTID)](https://ctid.mitre.org/projects/)** `E078` | 🟩 MITRE / CTID | Expansão do ATLAS com técnicas, filtro de maturidade e emulação para sistemas de IA. | 06/05/2026 | IA | P2 |
| ✅ | **[SPARTA](https://sparta.aerospace.org/)** `E095` | ◻️ Aerospace Corporation | TTPs contra espaçonaves e segmentos espaciais. | v4.0 (via D3FEND 1.6.0) | Espaço | P2 |

<details><summary>Notas e relações</summary>

- **ATLAS** — entrega: Cenários e técnicas de ameaça para IA. 16 táticas, 120 técnicas, 88 subtécnicas, 40 mitigações e 73 estudos de caso (CHANGELOG oficial). Use dist/ATLAS-latest.yaml; dist/ATLAS.yaml foi depreciado. ↔ ATT&CK, Secure AI (CTID), ATLAS Data.
- **ATT&CK** — entrega: Técnicas e procedimentos com evidência. v19 dividiu Defense Evasion em Stealth (TA0005) e Defense Impairment (TA0112); v20 trouxe técnicas de IA (prompt injection direta e indireta T1699/T1698, AI-Enabled Exfiltration T1700) e anti-automação (T1696). Enterprise v20: 227 técnicas, 479 subtécnicas, 703 Detection Strategies, 1.770 Analytics. Seções do site: Matrices, Tactics, Techniques, Mitigations, Assets (ICS), Detection Strategies, Analytics, Data Components, Groups, Software e Campaigns. ↔ CAPEC, D3FEND, Engage, CAR, Sigma, Atomic Red Team, RE&CT, Mappings Explorer, ATT&CK Detection Strategies e Analytics.
- **ATT&CK for ICS** — entrega: Cenários OT com técnicas, ativos e mitigações. v20: 12 táticas, 78 técnicas, 26 subtécnicas, 18 Assets, 106 Detection Strategies, 302 Analytics. Subtécnicas existem desde a v19. ↔ ATT&CK, Defending OT with ATT&CK, D3FEND, ESTM.
- **AADAPT** — entrega: Cenários de ameaça para ativos digitais. ↔ ATT&CK, Fight Fraud Framework.
- **ATT&CK Mobile** — entrega: Cenários mobile e requisitos de telemetria. v20: 12 táticas, 78 técnicas, 47 subtécnicas, 124 Detection Strategies, 211 Analytics. Relevante para fraude em mobile banking. ↔ ATT&CK, Engage.
- **CAPEC** — entrega: Padrões aplicáveis ao desenho do sistema. Related_Weakness liga a CWE; Taxonomy_Mapping liga ao ATT&CK. ↔ CWE, ATT&CK.
- **CAVEaT** — entrega: Cenários cloud e requisitos defensivos. ↔ ATT&CK.
- **DISARM** — entrega: Cenários e contramedidas de desinformação. Inspirado no ATT&CK; não é MITRE. Sucessor do AMITT. ↔ RE&CT, MISP Galaxy.
- **ESTM** — entrega: Cenários para avaliação de sistemas embarcados. Parceria com a Força Aérea dos EUA (CROWS). ↔ EMB3D.
- **FiGHT** — entrega: Modelo de ameaças de telecomunicações. Não confundir com o Fight Fraud Framework (E045). ↔ ATT&CK.
- **Fight Fraud Framework** — entrega: Cenários e hipóteses de fraude. Útil para clientes financeiros (Pix, mobile banking). ↔ ATT&CK, AADAPT.
- **Insider Threat TTP KB** — entrega: Hipóteses de investigação contextualizadas. ↔ ATT&CK.
- **LOLBAS** — entrega: Lista de binários para hipóteses de detecção. ↔ ATT&CK, Sigma.
- **Secure AI (CTID)** — entrega: Cenários de IA priorizados e testáveis. ↔ ATLAS.
- **SPARTA** — entrega: Cenários de ameaça espacial. Não é MITRE; o D3FEND for Space mapeia o SPARTA. ↔ D3FEND.

</details>

<a id="modelagem"></a>
## 🧭 Como representar o cenário

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[Attack Flow](https://github.com/center-for-threat-informed-defense/attack-flow)** `E032` | 🟩 MITRE / CTID | Representar sequência, condições e ramificações de ataques. | v4.1.0 · 14/10/2026 | Enterprise, ICS/OT | P1 |
| ⏸️ | **[Defending OT with ATT&CK](https://github.com/center-for-threat-informed-defense/defending-ot-with-attack)** `E048` | 🟩 MITRE / CTID | Adaptar coleções de ameaças a ambientes OT. | — | ICS/OT | P1 |
| ❔ | **[EMB3D](https://emb3d.mitre.org/)** `E005` | 🟦 MITRE | Relacionar propriedades de dispositivos embarcados a ameaças e mitigações. | — | Embarcados | P1 |
| ⏸️ | **[Threat Modeling with ATT&CK](https://github.com/center-for-threat-informed-defense/threat-modeling-with-attack)** `E047` | 🟩 MITRE / CTID | Integrar ATT&CK a uma metodologia de threat modeling. | — | Enterprise | P1 |
| ✅ | **[Top ATT&CK Techniques](https://github.com/center-for-threat-informed-defense/top-attack-techniques)** `E036` | 🟩 MITRE / CTID | Priorizar técnicas usando o método e contexto do projeto. | — | Enterprise | P1 |
| ⏸️ | **[Defending IaaS with ATT&CK](https://github.com/center-for-threat-informed-defense/defending-iaas-with-attack)** `E050` | 🟩 MITRE / CTID | Selecionar técnicas relevantes para Linux IaaS. | — | Cloud | P2 |
| ❔ | **[Unified Kill Chain](https://www.unifiedkillchain.com/)** `E096` | 🟨 Paul Pols | Combinar Kill Chain e ATT&CK em fases de ataque ponta a ponta. | — | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **Attack Flow** — entrega: Fluxo de ataque comunicável. v4.1 trouxe integração com D3FEND. ↔ ATT&CK, D3FEND, Technique Inference Engine.
- **Defending OT with ATT&CK** — entrega: Coleção contextual para OT. ↔ ATT&CK for ICS, D3FEND.
- **EMB3D** — entrega: Modelo de ameaças de dispositivo. ↔ ESTM, CWE.
- **Threat Modeling with ATT&CK** — entrega: Modelo conectado a comportamentos adversários. ↔ ATT&CK, D3FEND.
- **Top ATT&CK Techniques** — entrega: Lista inicial de técnicas; adaptar ao ambiente. ↔ ATT&CK, Technique Inference Engine.
- **Defending IaaS with ATT&CK** — entrega: Coleção de ameaças IaaS. ↔ ATT&CK, Mappings Explorer.
- **Unified Kill Chain** — entrega: Narrativa de ataque por fase. ↔ ATT&CK.

</details>

<a id="telemetria"></a>
## 📡 O que observar

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[DeTT&CT](https://github.com/rabobank-cdc/DeTTECT)** `E055` | 🟨 Rabobank / comunidade | Pontuar qualidade de dados, visibilidade e detecção. | v2.2.0 · 21/01/2026 | Enterprise, Mobile | P1 |
| ✅ | **[Dettectinator](https://github.com/siriussecurity/dettectinator)** `E118` | 🟨 Sirius Security / comunidade | Automatizar criação e atualização dos YAMLs DeTT&CT a partir de fontes SIEM/EDR. | — | Enterprise | P1 |
| ⏸️ | **[Sensor Mappings to ATT&CK](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack)** `E043` | 🟩 MITRE / CTID | Relacionar sensores e eventos a comportamentos. | — | Enterprise | P1 |
| ❔ | **[D3TECT — seleção estratégica de fontes](https://ucrisportal.univie.ac.at/en/publications/strategic-selection-of-data-sources-for-cyber-attack-detection-in/)** `E128` | ◻️ Kern, Skopik, Landauer e Weippl / pesquisa acadêmica | Estudar seleção e priorização de fontes de dados considerando restrições operacionais. | SAC 2022 | Enterprise | P2 |
| ❔ | **[OSSEM](https://github.com/OTRF/OSSEM)** `E087` | 🟨 OTRF | Padronizar e documentar eventos de segurança e seus campos. | — | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **DeTT&CT** — entrega: YAMLs e layers Navigator. Suporta ATT&CK v18 (modelo Data Components → Analytics → Detection Strategies). Suporte a v19/v20 não declarado. ↔ ATT&CK, Navigator, Sensor Mappings to ATT&CK.
- **Dettectinator** — entrega: Inventário de fontes e detecções para layers Navigator. Importação de regras não comprova eficácia; confirmar suporte dos plugins e compatibilidade com a versão ATT&CK. ↔ DeTT&CT, Navigator, OSSEM.
- **Sensor Mappings to ATT&CK** — entrega: Plano de telemetria. ↔ DeTT&CT, OSSEM.
- **D3TECT — seleção estratégica de fontes** — entrega: Método para justificar investimento e lacunas de telemetria. Artigo: Strategic selection of data sources for cyber attack detection in enterprise networks: A survey and approach. DOI 10.1145/3477314.3507022. D3TECT não é DeTT&CT e não é projeto MITRE. ↔ Sensor Mappings to ATT&CK, DeTT&CT, OSSEM.
- **OSSEM** — entrega: Dicionário de dados e modelo comum. ↔ CAR, Sensor Mappings to ATT&CK.

</details>

<a id="deteccao"></a>
## 🔎 Como detectar e avaliar

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[Ambiguous Techniques](https://ctid.mitre.org/projects/ambiguous-techniques/)** `E054` | 🟩 MITRE / CTID | Distinguir uso benigno de técnicas e contexto malicioso. | fev/2026 | Enterprise | P1 |
| ✅ | **[ATT&CK Detection Strategies e Analytics](https://attack.mitre.org/detectionstrategies/)** `E117` | 🟦 MITRE | Modelo de detecção nativo do ATT&CK desde a v18: técnica → Detection Strategy → Analytic → Data Component. | v20.0 | Enterprise, Mobile, ICS/OT | P1 |
| ⏸️ | **[CAR](https://car.mitre.org/)** `E011` | 🟦 MITRE | Consultar hipóteses e analíticas explicadas com base em ATT&CK. | — | Enterprise | P1 |
| ✅ | **[pySigma e sigma-cli](https://github.com/SigmaHQ/pySigma)** `E089` | 🟨 SigmaHQ | Converter regras Sigma para o backend do SIEM. | pySigma 2.0.1 · sigma-cli 3.1.0 (PyPI) | Enterprise, Cloud | P1 |
| ✅ | **[Sigma](https://github.com/SigmaHQ/sigma)** `E057` | 🟨 SigmaHQ | Representar e compartilhar regras de detecção. | r2026-07-01 | Enterprise, Cloud | P1 |
| ✅ | **[Summiting the Pyramid](https://github.com/center-for-threat-informed-defense/summiting-the-pyramid)** `E041` | 🟩 MITRE / CTID | Avaliar robustez e qualidade de analíticas. | release 10/09/2026 | Enterprise | P1 |
| 🧊 | **[Atomic Threat Coverage](https://github.com/atc-project/atomic-threat-coverage)** `E085` | 🟨 ATC Project | Gerar base de conhecimento unindo Sigma, RE&CT e ATT&CK. | — | Enterprise | P2 |
| ❔ | **[BZAR](https://github.com/mitre-attack/bzar)** `E012` | 🟦 MITRE | Analisar SMB/RPC com scripts Zeek orientados a comportamentos ATT&CK. | — | Enterprise | P2 |
| 🧊 | **[CARET](https://github.com/mitre-attack/caret)** `E109` | 🟦 MITRE | Visualizar relações entre analytics do CAR, técnicas, grupos e dados necessários. | — | Enterprise | P2 |
| ⏸️ | **[Cloud Analytics](https://github.com/center-for-threat-informed-defense/cloud-analytics)** `E042` | 🟩 MITRE / CTID | Estudar analíticas comportamentais para cloud. | — | Cloud | P2 |
| ✅ | **[Elastic Detection Rules](https://github.com/elastic/detection-rules)** `E063` | 🟧 Elastic | Estudar regras e workflows de detecção. | — | Enterprise, Cloud | P2 |
| ✅ | **[Elastic Protections Artifacts](https://github.com/elastic/protections-artifacts)** `E123` | 🟧 Elastic | Estudar lógica de proteção de endpoint, incluindo regras comportamentais e YARA. | — | Enterprise | P2 |
| ⏸️ | **[Security Datasets](https://github.com/OTRF/Security-Datasets)** `E064` | 🟨 OTRF | Reproduzir eventos de segurança para pesquisa. | — | Enterprise | P2 |
| ✅ | **[Splunk Security Content](https://github.com/splunk/security_content)** `E062` | 🟧 Splunk | Estudar conteúdo de detecção e investigação. | — | Enterprise, Cloud | P2 |
| ✅ | **[Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook)** `E086` | 🟨 OTRF | Estudar hunting por técnica com notebooks e datasets. | — | Enterprise | P2 |
| ✅ | **[TTP-Based Hunting](https://www.mitre.org/news-insights/publication/ttp-based-hunting)** `E071` | 🟦 MITRE | Organizar hunting orientado a comportamentos. | — | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **Ambiguous Techniques** — entrega: Enriquecimento e redução de ambiguidades. ↔ ATT&CK Detection Strategies e Analytics, Summiting the Pyramid.
- **ATT&CK Detection Strategies e Analytics** — entrega: Requisitos de dados e lógica de detecção por técnica. Substituiu os Data Sources como objeto de primeira classe na v18. ↔ ATT&CK, CAR, DeTT&CT, Summiting the Pyramid.
- **CAR** — entrega: Pseudocódigo e requisitos de dados. Sem atualização relevante desde mai/2025. As Detection Strategies/Analytics do ATT&CK (E075) ocupam esse papel. ↔ ATT&CK, OSSEM, BZAR.
- **pySigma e sigma-cli** — entrega: Regras na linguagem do SIEM com pipeline de campos. ↔ Sigma.
- **Sigma** — entrega: Regras adaptadas e testadas no backend. Tags attack.tXXXX nas regras. ↔ ATT&CK, pySigma e sigma-cli, Summiting the Pyramid.
- **Summiting the Pyramid** — entrega: Avaliação de resistência à evasão. Versão 2026 inclui cobertura de implementação e qualidade de detecção. ↔ CAR, Sigma, ATT&CK Detection Strategies e Analytics.
- **Atomic Threat Coverage** — entrega: Referência histórica de arquitetura. Sem atualização desde 2022. ↔ Sigma, RE&CT, ATT&CK.
- **BZAR** — entrega: Referência de detecção de rede. ↔ CAR.
- **CARET** — entrega: Referência histórica de relação analítica–técnica. Sem atualização desde ago/2020. ↔ CAR.
- **Cloud Analytics** — entrega: Blueprint e hipóteses de detecção. ↔ ATT&CK.
- **Elastic Detection Rules** — entrega: Analíticas adaptadas para Elastic. Elastic License v2. ↔ ATT&CK.
- **Elastic Protections Artifacts** — entrega: Referências de detecção e prevenção para endpoint. Distinto de elastic/detection-rules. README declara Elastic License 2.0; não tratar como Apache/MIT. ↔ Elastic Detection Rules, Sigma.
- **Security Datasets** — entrega: Dados para testes e replay. ↔ Threat Hunter Playbook, Sigma.
- **Splunk Security Content** — entrega: Analíticas adaptadas para Splunk. ↔ ATT&CK, Splunk Attack Range.
- **Threat Hunter Playbook** — entrega: Hipótese de hunting reproduzível. ↔ Security Datasets, TTP-Based Hunting, ATT&CK.
- **TTP-Based Hunting** — entrega: Hipóteses e espaço de análise. ↔ ATT&CK, Threat Hunter Playbook.

</details>

<a id="defesa"></a>
## 🛡️ Como reduzir exposição

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[D3FEND](https://d3fend.mitre.org/)** `E002` | 🟦 MITRE | Relacionar contramedidas e artefatos digitais em uma ontologia defensiva. | ontologia 1.6.0 · 31/08/2026 | Enterprise, ICS/OT, Espaço | P1 |
| ✅ | **[Mappings Explorer](https://github.com/center-for-threat-informed-defense/mappings-explorer)** `E037` | 🟩 MITRE / CTID | Explorar relações entre controles e comportamentos ATT&CK. | — | Enterprise, Cloud | P1 |
| ❔ | **[CREF Navigator](https://crefnavigator.mitre.org/)** `E020` | 🟦 MITRE / referência NIST | Explorar relações de engenharia de resiliência cibernética. | — | Geral | P2 |
| ✅ | **[D3FEND CAD](https://d3fend.mitre.org/)** `E077` | 🟦 MITRE | Diagramar cenários ataque–artefato–defesa a partir da ontologia D3FEND. | — | Enterprise, ICS/OT, Espaço | P2 |
| ✅ | **[Mappings Editor](https://github.com/center-for-threat-informed-defense/mappings-editor)** `E049` | 🟩 MITRE / CTID | Criar mapeamentos de capacidades para ATT&CK; beta na descrição consultada. | beta público | Enterprise | P2 |
| ✅ | **[Threat-Informed Defense for Cloud Security](https://www.mitre.org/news-insights/news-release/mitre-center-threat-informed-defense-and-industry-map-cloud-security)** `E081` | 🟩 MITRE / CTID | Relacionar controles de nuvem a comportamentos adversários. | 27/01/2026 | Cloud | P2 |

<details><summary>Notas e relações</summary>

- **D3FEND** — entrega: Hipóteses de controles a validar. 1.5.0 atualizou para ATT&CK v19.0 e mapeou ICS T0800–T0895. Issue #709: mapeamentos ainda citam técnicas revogadas na v19; validar contra a v20. ↔ ATT&CK, CWE, D3FEND CAD, Unified Kill Chain.
- **Mappings Explorer** — entrega: Crosswalk documentado de capacidades. NIST 800-53, CVE/KEV, AWS/Azure/GCP, M365, VERIS, CSA CCM e CIS Controls (out/2026). ↔ ATT&CK, CVE, NIST CSF 2.0, CISA KEV.
- **CREF Navigator** — entrega: Decisões arquiteturais de resiliência. Base conceitual do NIST SP 800-160 v2. ↔ NIST CSF 2.0.
- **D3FEND CAD** — entrega: Grafo CAD exportável com contramedidas justificadas. Biblioteca e IDE renovados em dez/2025; importa relatórios do Caldera. ↔ D3FEND, Apache Caldera, Attack Flow.
- **Mappings Editor** — entrega: Mapeamentos com justificativa. ↔ Mappings Explorer.
- **Threat-Informed Defense for Cloud Security** — entrega: Controles cloud priorizados por técnica. ↔ Mappings Explorer, Defending IaaS with ATT&CK.

</details>

<a id="engano"></a>
## 🎭 Como enganar e engajar

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ⏸️ | **[Engage](https://engage.mitre.org/)** `E003` | 🟦 MITRE | Planejar deception, denial e engajamento de adversários. | v1.0 | Enterprise, ICS/OT, Mobile | P1 |

<details><summary>Notas e relações</summary>

- **Engage** — entrega: Plano de engajamento com objetivos e limites. Sucessor do Shield (aposentado em 2021). Método estável; repositório com pouca atividade. ↔ ATT&CK.

</details>

<a id="validacao"></a>
## 🧪 Como validar

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ⏸️ | **[Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library)** `E031` | 🟩 MITRE / CTID | Planejar emulações baseadas em TTPs documentadas. | — | Enterprise | P1 |
| ✅ | **[Apache Caldera](https://caldera.apache.org/)** `E013` | 🟫 Apache Software Foundation (código originado na MITRE) | Orquestrar emulação adversária em ambientes autorizados. | 5.3.0 (tag) | Enterprise, ICS/OT | P1 |
| ✅ | **[Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)** `E058` | 🟨 Red Canary / comunidade | Validar comportamentos isolados em laboratório. | — | Enterprise, Cloud | P1 |
| ✅ | **[Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)** `E100` | 🟧 Red Canary | Executar testes Atomic com PowerShell, incluindo pré-requisitos e limpeza. | v2.3.0 (tag) | Enterprise | P1 |
| ✅ | **[OpenAEV (anteriormente OpenBAS)](https://github.com/OpenAEV-Platform/openaev)** `E119` | 🟧 Filigran / comunidade | Planejar e acompanhar campanhas, simulações e exercícios com contexto de inteligência. | — | Enterprise, Cloud | P1 |
| ✅ | **[Stratus Red Team](https://github.com/DataDog/stratus-red-team)** `E090` | 🟧 Datadog | Emular técnicas em AWS, Azure, GCP e Kubernetes. | v2.37.1 (tag) | Cloud | P1 |
| ✅ | **[Threatest](https://github.com/DataDog/threatest)** `E120` | 🟧 Datadog | Testar de ponta a ponta a geração de telemetria e alertas associados a uma execução. | — | Enterprise, Cloud | P1 |
| ✅ | **[TTPForge](https://github.com/facebookincubator/TTPForge)** `E121` | 🟧 Meta / comunidade | Empacotar TTPs em simulações repetíveis descritas em YAML. | — | Enterprise | P1 |
| ⏸️ | **[ATLAS Arsenal (plugin CALDERA)](https://github.com/mitre-atlas/arsenal)** `E125` | 🟦 MITRE ATLAS | Estudar emulação de comportamentos ATLAS em sistemas de aprendizado de máquina. | — | IA | P2 |
| 🧊 | **[ATT&CK Arsenal](https://github.com/mitre-attack/attack-arsenal)** `E108` | 🟦 MITRE | Recursos de red team e emulação publicados pela equipe ATT&CK. | — | Enterprise | P2 |
| ✅ | **[ATT&CK Evaluations](https://evals.mitre.org/)** `E014` | 🟦 MITRE | Examinar avaliações públicas e suas metodologias. | Enterprise 2025 (ER7) | Enterprise, Cloud | P2 |
| ❔ | **[Infection Monkey](https://github.com/guardicore/monkey)** `E093` | 🟧 Akamai (Guardicore) | Simular movimentação lateral e gerar relatório por técnica. | v2.3.0 (tag) | Enterprise | P2 |
| ⏸️ | **[Micro Emulation Plans](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master/micro_emulation_plans)** `E080` | 🟩 MITRE / CTID | Emular comportamentos compostos curtos, sem uma campanha inteira. | — | Enterprise | P2 |
| ⏸️ | **[PurpleSharp](https://github.com/mvelazc0/PurpleSharp)** `E092` | 🟨 Mauricio Velazco | Simular técnicas em Active Directory e Windows. | v1.3 (tag) | Enterprise | P2 |
| ✅ | **[Splunk Attack Range](https://github.com/splunk/attack_range)** `E061` | 🟧 Splunk | Montar ambiente instrumentado para exercícios. | — | Enterprise, Cloud | P2 |
| ✅ | **[VECTR](https://github.com/SecurityRiskAdvisors/VECTR)** `E091` | 🟧 Security Risk Advisors | Registrar campanhas purple team e resultados por técnica. | ce-9.14.1 (tag) | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **Adversary Emulation Library** — entrega: Plano de exercício e evidências. ↔ Apache Caldera, Micro Emulation Plans, ATT&CK Evaluations.
- **Apache Caldera** — entrega: Evidência de exercícios e validação. Doado à Apache Software Foundation: Apache Caldera (Incubating), repo apache/caldera. ↔ ATT&CK, Adversary Emulation Library, Micro Emulation Plans, D3FEND.
- **Atomic Red Team** — entrega: Resultados de testes por técnica. Um diretório por técnica (atomics/TXXXX). ↔ ATT&CK, Invoke-AtomicRedTeam.
- **Invoke-AtomicRedTeam** — entrega: Execução registrada de testes atômicos. ↔ Atomic Red Team.
- **OpenAEV (anteriormente OpenBAS)** — entrega: Campanha de validação e registro de lacunas. OpenBAS foi renomeado para OpenAEV. README distingue CE Apache-2.0 e EE com licença própria; verificar funcionalidades por edição. ↔ OpenCTI, Adversary Emulation Library, VECTR.
- **Stratus Red Team** — entrega: Execução cloud com detonação e limpeza. ↔ Atomic Red Team, ATT&CK.
- **Threatest** — entrega: Teste repetível com correlação entre execução e evidência. CLI/framework Go; matchers e detonators dependem da plataforma. A existência de um alerta não prova cobertura de toda a técnica. ↔ Stratus Red Team, Elastic Detection Rules, Atomic Red Team.
- **TTPForge** — entrega: Procedimentos versionados para exercícios purple team. Complementa ferramentas de avaliação; definir pré-condições, limpeza e critérios de aceite por procedimento. ↔ Atomic Red Team, Adversary Emulation Library, VECTR.
- **ATLAS Arsenal (plugin CALDERA)** — entrega: Referência de cenários e abilities para laboratório. Não confundir com ATT&CK Arsenal. Último push consultado: 2023; documentação cita dependências antigas. Compatibilidade atual não testada. ↔ ATLAS, Apache Caldera.
- **ATT&CK Arsenal** — entrega: Referência histórica de emulação. Sem atualização desde abr/2021. Fontes divergem sobre o arquivamento (listagem da org vs. checagem de 23/10/2026); confirme na página do repositório. Prefira Adversary Emulation Library e Apache Caldera. ↔ Adversary Emulation Library, Apache Caldera.
- **ATT&CK Evaluations** — entrega: Evidência contextual de capacidade; não ranking universal. Edição 2026 usa a métrica TES (DQI + PQI). Não é ranking universal. ↔ ATT&CK, Adversary Emulation Library.
- **Infection Monkey** — entrega: Relatório de exposição mapeado ao ATT&CK. ↔ ATT&CK.
- **Micro Emulation Plans** — entrega: Execução focada com eventos esperados. ↔ Adversary Emulation Library, Apache Caldera.
- **PurpleSharp** — entrega: Telemetria gerada para validar detecção. ↔ Atomic Red Team.
- **Splunk Attack Range** — entrega: Telemetria de laboratório. ↔ Atomic Red Team, Splunk Security Content.
- **VECTR** — entrega: Histórico de testes e evolução da defesa. ↔ Atomic Red Team, Apache Caldera.

</details>

<a id="resposta"></a>
## 🚑 Como responder e investigar

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[Hayabusa](https://github.com/Yamato-Security/hayabusa)** `E101` | 🟨 Yamato Security | Triagem forense rápida de Windows Event Logs com regras Sigma. | v4.2.0 (tag) | Enterprise | P1 |
| ⏸️ | **[RE&CT](https://github.com/atc-project/atc-react)** `E056` | 🟨 ATC Project | Organizar ações e playbooks de resposta a incidentes. | — | Enterprise | P1 |
| ✅ | **[AWS Customer Playbook Framework](https://github.com/aws-samples/aws-customer-playbook-framework)** `E124` | 🟧 AWS | Adaptar exemplos de playbooks de resposta a cenários AWS. | — | Cloud | P2 |
| ✅ | **[Chainsaw](https://github.com/WithSecureLabs/chainsaw)** `E102` | 🟧 WithSecure | Busca e caça em artefatos Windows (EVTX, MFT) com Sigma. | v2.17.1 (tag) | Enterprise | P2 |
| ✅ | **[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)** `E068` | ⬜ NIST | Integrar resposta a incidentes à gestão de risco. | Rev. 3 | Geral | P2 |

<details><summary>Notas e relações</summary>

- **Hayabusa** — entrega: Linha do tempo de DFIR com técnicas ATT&CK. ↔ Sigma, Chainsaw.
- **RE&CT** — entrega: Matriz de ações e playbooks revisados. Seis estágios: Preparation → Lessons Learned. ↔ ATT&CK, DISARM, D3FEND.
- **AWS Customer Playbook Framework** — entrega: Procedimentos de resposta ajustados às contas e serviços. Relação com ATT&CK é composição editorial, não crosswalk automático. README informa traduções automáticas não revisadas; validar contexto e permissões. ↔ RE&CT, NIST SP 800-61 Rev. 3, Stratus Red Team.
- **Chainsaw** — entrega: Achados forenses por regra e técnica. ↔ Sigma, Hayabusa.
- **NIST SP 800-61 Rev. 3** — entrega: Processos de resposta e melhoria contínua. ↔ RE&CT, NIST CSF 2.0.

</details>

<a id="vulnerabilidade"></a>
## 🩹 Que fraquezas existem

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** `E083` | ⬛ CISA | Saber quais CVEs têm exploração confirmada. | — | Enterprise | P1 |
| ✅ | **[CVE](https://www.cve.org/)** `E010` | 🟦 Programa CVE / ecossistema MITRE | Identificar vulnerabilidades publicamente divulgadas. | registros JSON 5.x | Enterprise | P2 |
| ✅ | **[CVSS](https://www.first.org/standards/)** `E069` | ⬜ FIRST | Caracterizar severidade técnica de vulnerabilidades. | — | Geral | P2 |
| ✅ | **[CWE](https://cwe.mitre.org/)** `E009` | 🟦 MITRE | Classificar tipos de fraquezas de software e hardware. | 4.20 · 30/04/2026 | Enterprise, Embarcados | P2 |
| ⏸️ | **[CWE Calculator](https://github.com/center-for-threat-informed-defense/cwe-calculator)** `E051` | 🟩 MITRE / CTID | Apoiar priorização empírica de fraquezas. | — | Enterprise | P2 |
| ✅ | **[EPSS](https://www.first.org/epss/)** `E070` | ⬜ FIRST | Estimar probabilidade de exploração para priorização. | — | Geral | P2 |
| ✅ | **[NVD](https://nvd.nist.gov/)** `E084` | ⬛ NIST | Enriquecer CVEs com CVSS, CPE e CWE. | API 2.0 | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **CISA KEV** — entrega: Fila de correção priorizada. ↔ CVE, Mappings Explorer, EPSS.
- **CVE** — entrega: Identificadores e registros de vulnerabilidade. MITRE atua como Secretariat; financiamento via CISA renegociado após a crise de abril/2025. ↔ CWE, NVD, CISA KEV, Mappings Explorer.
- **CVSS** — entrega: Vetor e pontuação de severidade. ↔ CVE.
- **CWE** — entrega: Taxonomia de causas de vulnerabilidades. ↔ CAPEC, CVE, D3FEND.
- **CWE Calculator** — entrega: Pontuação contextual de CWEs. ↔ CWE.
- **EPSS** — entrega: Probabilidade estimada; combinar com exposição e impacto. ↔ CVE, CISA KEV.
- **NVD** — entrega: CVE enriquecido e ligado a produto e fraqueza. ↔ CVE, CWE, CVSS.

</details>

<a id="cti"></a>
## 🕵️ Como produzir e compartilhar CTI

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[Contribuir com o ATT&CK](https://attack.mitre.org/resources/engage-with-attack/contribute/)** `E110` | 🟦 MITRE | Enviar novas técnicas, procedimentos, grupos, softwares e correções para a equipe do ATT&CK. | — | Enterprise, Mobile, ICS/OT | P1 |
| ⏸️ | **[CTI Blueprints](https://github.com/center-for-threat-informed-defense/cti-blueprints)** `E034` | 🟩 MITRE / CTID | Estruturar relatórios de inteligência acionáveis. | — | Enterprise | P1 |
| ✅ | **[ATT&CK Powered Suit](https://github.com/center-for-threat-informed-defense/attack-powered-suit)** `E038` | 🟩 MITRE / CTID | Consultar ATT&CK por extensão de navegador. | — | Enterprise | P2 |
| ❔ | **[D3FEND Extractors](https://d3fend.mitre.org/tools/)** `E127` | 🟦 MITRE D3FEND | Explorar extratores de referências ATT&CK, D3FEND, artefatos digitais e CWE em texto. | — | Geral | P2 |
| ⏸️ | **[Decider](https://github.com/cisagov/decider)** `E082` | ⬛ CISA (com HSSEDI/MITRE) | Guiar o mapeamento de relatos para técnicas ATT&CK por perguntas. | v3.0.0 (tag) | Enterprise | P2 |
| ❔ | **[ECHO](https://www.mitre.org/news-insights/fact-sheet/enhanced-cti-sharing-partner-organizations)** `E021` | 🟦 MITRE | Conhecer aplicação de extração e contextualização de CTI. | — | Enterprise | P2 |
| ✅ | **[MISP Galaxy](https://github.com/MISP/misp-galaxy)** `E060` | 🟨 MISP Project | Contextualizar eventos com clusters de inteligência. | — | Enterprise, IA, Desinformação | P2 |
| ✅ | **[OpenCTI](https://github.com/OpenCTI-Platform/opencti)** `E059` | 🟨 Filigran / comunidade | Organizar entidades e relações de inteligência. | — | Enterprise | P2 |
| ⏸️ | **[Sightings Ecosystem](https://github.com/center-for-threat-informed-defense/sightings_ecosystem)** `E044` | 🟩 MITRE / CTID | Estudar observações e prevalência de técnicas. | — | Enterprise | P2 |
| ✅ | **[Technique Inference Engine](https://github.com/center-for-threat-informed-defense/technique-inference-engine)** `E040` | 🟩 MITRE / CTID | Inferir técnicas associadas a comportamentos observados. | — | Enterprise | P2 |
| ⏸️ | **[TRAM](https://github.com/center-for-threat-informed-defense/tram)** `E033` | 🟩 MITRE / CTID | Apoiar mapeamento de relatórios de CTI para ATT&CK. | — | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **Contribuir com o ATT&CK** — entrega: Contribuição com evidência que pode render crédito como contribuidor. Contribuições aceitas aparecem no campo Contributors das páginas. ↔ ATT&CK, Attack Flow.
- **CTI Blueprints** — entrega: Relatório com contexto e decisões. ↔ ATT&CK.
- **ATT&CK Powered Suit** — entrega: Apoio à análise de textos. ↔ ATT&CK.
- **D3FEND Extractors** — entrega: Anotações e relações candidatas para revisão. Agrupa ferramentas do portal, sem contar cada extrator separadamente. Extração não valida a semântica do mapeamento nem demonstra eficácia de contramedidas. ↔ D3FEND, CAPEC, CWE, D3FEND CAD.
- **Decider** — entrega: Mapeamento ATT&CK revisável. ↔ ATT&CK, TRAM.
- **MISP Galaxy** — entrega: Enriquecimento e classificação. ↔ ATT&CK, ATLAS, DISARM.
- **OpenCTI** — entrega: Grafo de CTI com proveniência. ↔ ATT&CK, MISP Galaxy.
- **Sightings Ecosystem** — entrega: Contexto empírico de priorização. ↔ ATT&CK.
- **Technique Inference Engine** — entrega: Hipóteses; não fatos de inteligência. ↔ ATT&CK, Attack Flow, Top ATT&CK Techniques.
- **TRAM** — entrega: Sugestões de técnicas para revisão humana. ↔ ATT&CK, Decider.

</details>

<a id="maturidade"></a>
## 📈 Como evoluir o programa

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[INFORM](https://github.com/center-for-threat-informed-defense/inform)** `E053` | 🟩 MITRE / CTID | Avaliar adoção de defesa orientada por ameaças. | 08/01/2026 | Geral | P1 |
| ✅ | **[11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)** `E072` | 🟦 MITRE | Estudar desenho e evolução de um SOC. | — | Geral | P2 |

<details><summary>Notas e relações</summary>

- **INFORM** — entrega: Diagnóstico e plano de evolução. Substitui o M3TID (arquivado). ↔ 11 Strategies of a World-Class Cybersecurity Operations Center.
- **11 Strategies of a World-Class Cybersecurity Operations Center** — entrega: Plano operacional e de maturidade. ↔ INFORM.

</details>

<a id="dados"></a>
## 🗄️ Como consumir por código

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[ATLAS Data](https://github.com/mitre-atlas/atlas-data)** `E079` | 🟦 MITRE | Distribuir o ATLAS em YAML versionado (conteúdo AAAA.MM, formato semver). | conteúdo 2026.09 · formato 6.0.0 | IA | P1 |
| ✅ | **[ATT&CK Data Model](https://github.com/mitre-attack/attack-data-model)** `E029` | 🟦 MITRE | Validar e manipular dados ATT&CK com schemas TypeScript/Zod. | — | Enterprise | P1 |
| ✅ | **[ATT&CK STIX 2.0](https://github.com/mitre/cti)** `E027` | 🟦 MITRE | Consultar a representação STIX 2.0. | tag ATT&CK-v20.0 | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[ATT&CK STIX 2.1](https://github.com/mitre-attack/attack-stix-data)** `E026` | 🟦 MITRE | Consumir a base ATT&CK em formato estruturado. | v20.0 | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[ATT&CK Updates e Version History](https://attack.mitre.org/resources/updates/)** `E111` | 🟦 MITRE | Ler as notas de cada release e navegar versões antigas do site. | v20 · 13/10/2026 | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[mitreattack-python](https://github.com/mitre-attack/mitreattack-python)** `E028` | 🟦 MITRE | Consultar e transformar dados ATT&CK com Python. | 6.3.1 · 13/10/2026 (PyPI) | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[Navigator](https://github.com/mitre-attack/attack-navigator)** `E024` | 🟦 MITRE | Visualizar e anotar matrizes. | v5.3.2 | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[Splunk Attack Data](https://github.com/splunk/attack_data)** `E122` | 🟧 Splunk | Consumir datasets de ataques e reproduzir eventos para desenvolver e validar analíticas. | — | Enterprise, Cloud | P1 |
| ✅ | **[Workbench](https://github.com/mitre-attack/attack-workbench-frontend)** `E025` | 🟦 MITRE | Gerenciar extensões locais de ATT&CK. | v4.18.0-alpha.1 (tag) | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[Workbench Deployment](https://github.com/mitre-attack/attack-workbench-deployment)** `E074` | 🟦 MITRE | Subir o Workbench completo (frontend, REST API, banco e TAXII opcional) com Docker Compose ou Kubernetes. | — | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[Workbench TAXII Server](https://github.com/mitre-attack/attack-workbench-taxii-server)** `E030` | 🟦 MITRE | Servir coleções ATT&CK via TAXII. | — | Enterprise | P1 |
| ✅ | **[ATLAS Navigator](https://github.com/mitre-atlas/atlas-navigator)** `E104` | 🟦 MITRE | Visualizar e anotar a matriz ATLAS. | v4.5.5 (tag) | IA | P2 |
| ✅ | **[ATT&CK Sync](https://github.com/center-for-threat-informed-defense/attack-sync)** `E046` | 🟩 MITRE / CTID | Apoiar adoção de mudanças entre versões ATT&CK. | — | Enterprise | P2 |
| ✅ | **[ATT&CK TAXII 2.1 (público)](https://attack-taxii.mitre.org/)** `E099` | 🟦 MITRE | Servir o ATT&CK por TAXII 2.1. | — | Enterprise, Mobile, ICS/OT | P2 |
| ✅ | **[ATT&CK Website (código)](https://github.com/mitre-attack/attack-website)** `E075` | 🟦 MITRE | Consultar o código do site oficial e gerá-lo localmente, inclusive para uso offline ou em rede isolada. | — | Enterprise, Mobile, ICS/OT | P2 |
| ✅ | **[attackcti](https://github.com/OTRF/ATTACK-Python-Client)** `E088` | 🟨 OTRF | Consultar ATT&CK via TAXII em Python. | 0.6.4 · 19/12/2025 (PyPI) | Enterprise, Mobile, ICS/OT | P2 |
| ⏸️ | **[BRAWL public game 001](https://github.com/mitre/brawl-public-game-001)** `E126` | 🟦 MITRE | Estudar dados de um exercício automatizado de emulação adversária. | — | Enterprise | P2 |
| ✅ | **[stix2 (Python)](https://github.com/oasis-open/cti-python-stix2)** `E097` | ⬜ OASIS | Criar, validar e consultar objetos STIX 2.x. | 3.0.2 (PyPI) | Geral | P2 |
| ⏸️ | **[taxii2-client](https://github.com/oasis-open/cti-taxii-client)** `E098` | ⬜ OASIS | Consumir servidores TAXII 2.x. | 2.3.0 · 2021 (PyPI) | Geral | P2 |
| ✅ | **[Workbench REST API](https://github.com/mitre-attack/attack-workbench-rest-api)** `E073` | 🟦 MITRE | Backend do ATT&CK Workbench: API REST para criar e versionar extensões do ATT&CK. | v4.26.0-alpha.1 (tag) | Enterprise, Mobile, ICS/OT | P2 |

<details><summary>Notas e relações</summary>

- **ATLAS Data** — entrega: ATLAS-latest.yaml e manifesto de versões. dist/ATLAS.yaml está depreciado; use dist/ATLAS-latest.yaml. ↔ ATLAS.
- **ATT&CK Data Model** — entrega: Validação estrutural. ↔ ATT&CK STIX 2.1.
- **ATT&CK STIX 2.0** — entrega: Integração compatível com consumidores STIX 2.0. Também distribui o CAPEC em STIX. ↔ ATT&CK, CAPEC.
- **ATT&CK STIX 2.1** — entrega: Snapshots versionados de objetos e relações. Um bundle por versão (enterprise-attack-20.0.json) e um 'latest'; index.json lista coleções. ↔ ATT&CK, mitreattack-python.
- **ATT&CK Updates e Version History** — entrega: Plano de migração entre versões. Versões antigas: https://attack.mitre.org/resources/versions/. Changelog legível por máquina em /docs/changelogs/. ↔ ATT&CK STIX 2.1, mitreattack-python.
- **mitreattack-python** — entrega: Consultas e exportações reproduzíveis. MitreAttackData, exportação Excel, diffStix e layers. ↔ ATT&CK STIX 2.1, Navigator.
- **Navigator** — entrega: Layers JSON para comunicar prioridade e evidência. ↔ ATT&CK, DeTT&CT.
- **Splunk Attack Data** — entrega: Logs de teste com contexto de coleta. É a camada de dados, distinta de Attack Range e Security Content. Revisar sourcetype, timestamp e versão; usar download seletivo via Git LFS. ↔ Splunk Attack Range, Splunk Security Content, Security Datasets.
- **Workbench** — entrega: Coleções locais e anotações. ↔ ATT&CK, Workbench TAXII Server.
- **Workbench Deployment** — entrega: Instância interna do Workbench para técnicas e grupos da casa. Caminho mais curto para manter um ATT&CK local com extensões (ex.: grupos BR/LATAM do MSSP). ↔ Workbench, Workbench REST API, Workbench TAXII Server.
- **Workbench TAXII Server** — entrega: Intercâmbio de CTI. ↔ Workbench.
- **ATLAS Navigator** — entrega: Layers ATLAS. ↔ ATLAS, Navigator.
- **ATT&CK Sync** — entrega: Processo de atualização de bases. ↔ ATT&CK, mitreattack-python.
- **ATT&CK TAXII 2.1 (público)** — entrega: Coleções ATT&CK por API. ↔ ATT&CK STIX 2.1, attackcti, DeTT&CT.
- **ATT&CK Website (código)** — entrega: Espelho interno do site com a versão fixada. ↔ ATT&CK STIX 2.1, ATT&CK.
- **attackcti** — entrega: Consultas e exportações programáticas. ↔ ATT&CK TAXII 2.1 (público), mitreattack-python.
- **BRAWL public game 001** — entrega: Dataset de referência para pesquisa de detecção. Dataset histórico: último push consultado em 2020. Não representa versões atuais de sistemas ou distribuição de ataques; não é uma plataforma BRAWL completa. ↔ Apache Caldera, Security Datasets.
- **stix2 (Python)** — entrega: Objetos STIX válidos. ↔ STIX, mitreattack-python.
- **taxii2-client** — entrega: Coleções STIX baixadas. ↔ TAXII, ATT&CK TAXII 2.1 (público).
- **Workbench REST API** — entrega: Base ATT&CK própria acessível por API. ↔ Workbench, Workbench TAXII Server, Workbench Deployment.

</details>

<a id="conformidade"></a>
## ⚙️ Como automatizar conformidade

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ❔ | **[eMASSer](https://saf.mitre.org/)** `E019` | 🟦 MITRE | Integrar workflows de avaliação ao eMASS; acessar Apps → eMASSer. | — | Enterprise | P2 |
| ❔ | **[Heimdall](https://github.com/mitre/heimdall2)** `E016` | 🟦 MITRE | Visualizar e comparar resultados de avaliações. | — | Enterprise | P2 |
| ❔ | **[SAF](https://saf.mitre.org/)** `E015` | 🟦 MITRE | Automatizar avaliação e normalização de resultados de segurança. | — | Enterprise | P2 |
| ❔ | **[SAF CLI](https://github.com/mitre/saf)** `E017` | 🟦 MITRE | Normalizar saídas de ferramentas e apoiar pipelines de segurança. | — | Enterprise | P2 |
| ❔ | **[Vulcan](https://saf.mitre.org/)** `E018` | 🟦 MITRE | Criar e gerenciar orientação e baselines de segurança; acessar Apps → Vulcan. | — | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **eMASSer** — entrega: Integração de resultados de avaliação. ↔ SAF.
- **Heimdall** — entrega: Visão consolidada de conformidade. ↔ SAF.
- **SAF** — entrega: Resultados comparáveis de controles. ↔ Heimdall, SAF CLI.
- **SAF CLI** — entrega: Dados normalizados e validações. ↔ SAF.
- **Vulcan** — entrega: Baseline de requisitos. ↔ SAF.

</details>

<a id="padrao"></a>
## 📐 Padrões de base

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[ATT&CK Legal & Branding](https://attack.mitre.org/resources/legal-and-branding/)** `E114` | 🟦 MITRE | Termos de uso dos dados e regras de marca do ATT&CK. | — | Geral | P2 |
| ✅ | **[NIST CSF 2.0](https://www.nist.gov/cyberframework)** `E067` | ⬜ NIST | Organizar resultados de gestão de risco, incluindo Respond e Recover. | 2.0 | Geral | P2 |
| ✅ | **[STIX](https://oasis-open.github.io/cti-documentation/)** `E065` | ⬜ OASIS | Representar inteligência estruturada. | 2.1 | Geral | P2 |
| ✅ | **[TAXII](https://oasis-open.github.io/cti-documentation/taxii/intro.html)** `E066` | ⬜ OASIS | Transportar e compartilhar CTI. | 2.1 | Geral | P2 |

<details><summary>Notas e relações</summary>

- **ATT&CK Legal & Branding** — entrega: Checagem antes de redistribuir dados ou usar a marca. ↔ ATT&CK, ATT&CK STIX 2.1.
- **NIST CSF 2.0** — entrega: Perfil de resultados e responsabilidades. ↔ NIST SP 800-61 Rev. 3, Mappings Explorer.
- **STIX** — entrega: Objetos e relações de CTI. ↔ ATT&CK STIX 2.1, TAXII.
- **TAXII** — entrega: Coleções consumíveis por API. ↔ STIX, ATT&CK TAXII 2.1 (público).

</details>

<a id="formacao"></a>
## 🎓 Como aprender

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[ATT&CK — Learn More e FAQ](https://attack.mitre.org/resources/learn-more-about-attack/)** `E112` | 🟦 MITRE | Material oficial de introdução, treinamento e perguntas frequentes. | — | Enterprise, Mobile, ICS/OT | P1 |
| ✅ | **[ATT&CKcon](https://attack.mitre.org/resources/attackcon/)** `E113` | 🟦 MITRE | Conferência anual do ATT&CK, com palestras gravadas. | 7.0 · 27–28/10/2026, McLean (EUA) | Enterprise, Mobile, ICS/OT | P2 |
| ⏸️ | **[CTID Public Resources](https://github.com/center-for-threat-informed-defense/public-resources)** `E039` | 🟩 MITRE / CTID | Localizar materiais públicos do Center. | — | Geral | P2 |
| ⏸️ | **[CTID Workshop](https://github.com/center-for-threat-informed-defense/workshop)** `E052` | 🟩 MITRE / CTID | Acessar materiais de workshops do Center. | — | Geral | P2 |
| ✅ | **[eCTF](https://ectf.mitre.org/)** `E022` | 🟦 MITRE | Praticar segurança de sistemas embarcados em competição. | — | Embarcados | P2 |
| ❔ | **[Red Team Redemption](https://arxiv.org/abs/2408.15645)** `E129` | ◻️ Landauer, Mayer, Skopik, Wurzenberger e Kern | Estudar uma comparação estruturada de ferramentas de emulação adversária. | 2024 / TrustCom | Enterprise | P2 |

<details><summary>Notas e relações</summary>

- **ATT&CK — Learn More e FAQ** — entrega: Base comum de vocabulário para o time. FAQ: https://attack.mitre.org/resources/faq/ ↔ ATT&CK, ATT&CKcon.
- **ATT&CKcon** — entrega: Casos de uso da comunidade. ↔ ATT&CK.
- **eCTF** — entrega: Experiência de projeto e avaliação. ↔ EMB3D.
- **Red Team Redemption** — entrega: Critérios para seleção e benchmark de ferramentas. Compara nove ferramentas usando questionário com 80 questões. Ranking reflete a amostra e o período do estudo; não é ranking atualizado do mercado. ↔ Apache Caldera, Atomic Red Team, TTPForge.

</details>

## 🗄️ Itens históricos e depreciados

| Item | Situação |
|---|---|
| [attack-control-framework-mappings](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings) | Mapeamentos NIST migraram para Mappings Explorer, conforme descrição do repositório. |
| [security-stack-mappings](https://github.com/center-for-threat-informed-defense/security-stack-mappings) | Mapeamentos de stacks migraram para Mappings Explorer, conforme descrição do repositório. |
| [attack_to_cve](https://github.com/center-for-threat-informed-defense/attack_to_cve) | Mapeamentos CVE migraram para Mappings Explorer, conforme descrição do repositório. |
| [caldera_pathfinder](https://github.com/center-for-threat-informed-defense/caldera_pathfinder) | Plugin histórico de caminhos de rede; não recomendar instalação como componente atual sem revisão. |
| [attack_to_veris](https://github.com/center-for-threat-informed-defense/attack_to_veris) | Mapeamentos VERIS migraram para Mappings Explorer, conforme descrição do repositório. |
| [m3tid](https://github.com/center-for-threat-informed-defense/m3tid) | Referência histórica de maturidade; avaliar o projeto atual INFORM. Não assumir equivalência de versões ou scores. |
| [attack-workbench-collection-manager](https://github.com/center-for-threat-informed-defense/attack-workbench-collection-manager) | Marcado como deprecated; consultar a arquitetura atual do Workbench. |
| [MITRE Shield](https://shield.mitre.org/) | Aposentado em 18/10/2021; substituído pelo Engage (E003). shield.mitre.org redireciona. |
| [PRE-ATT&CK](https://attack.mitre.org/resources/updates/) | Absorvido no Enterprise como Reconnaissance (TA0043) e Resource Development (TA0042) na v8 (out/2020). |
| [pyattck](https://github.com/swimlane/pyattck) | Arquivado em 17/03/2026; último release 7.1.2 (2023). Migrar para mitreattack-python ou attackcti. |
| [ATT&CK Data Sources (objeto)](https://attack.mitre.org/resources/updates/) | Removidos na v18 (out/2025); substituídos por Data Components ligados a Analytics e Detection Strategies. |
| [T1562 Impair Defenses](https://attack.mitre.org/techniques/T1562/) | Revogada na v19 (28/04/2026) com a criação da tática Defense Impairment (TA0112). |
| [dist/ATLAS.yaml](https://github.com/mitre-atlas/atlas-data) | Arquivo depreciado; usar dist/ATLAS-latest.yaml (formato 6.0.0). |
| [mitre-attack/attack-scripts](https://github.com/mitre-attack/attack-scripts) | Scripts e biblioteca planejada; substituídos pelo mitreattack-python. Arquivado (dez/2023). |
| [mitre-attack/evals_caldera](https://github.com/mitre-attack/evals_caldera) | Plugin CALDERA da rodada 1 das ATT&CK Evaluations. Arquivado (set/2023). |
| [mitre-attack/joystick](https://github.com/mitre-attack/joystick) | Visualização de resultados das Evaluations. Arquivado (set/2023); use evals.mitre.org. |
| [mitre-attack/attack-datasources](https://github.com/mitre-attack/attack-datasources) | Pesquisa sobre Data Sources. Arquivado (set/2023); o modelo mudou na v18. |
| [mitre-attack/attack-datasources-stix-beta](https://github.com/mitre-attack/attack-datasources-stix-beta) | STIX beta da representação antiga de Data Sources. Arquivado (set/2023). |
| [mitre-attack/tram](https://github.com/mitre-attack/tram) | Versão antiga do TRAM. Arquivado (out/2021); a atual está no CTID (E033). |
| [mitre-attack/attack-evals](https://github.com/mitre-attack/attack-evals) | Site antigo das Evaluations. Arquivado (abr/2021); use evals.mitre.org. |
| [mitre-attack/attack-archives](https://github.com/mitre-attack/attack-archives) | Releases antigos do site. Arquivado (jul/2020); use Version History (E111). |

---

_Limites da verificação:_ Pesquisa documental; ferramentas não executadas. Campos ausentes: não coletados. archived=false não comprova manutenção ativa. pushed_at não equivale a último release. license_api não substitui leitura da licença. Status 'n/v' = não verificado. Tag Git indica marco publicado, não necessariamente release estável.

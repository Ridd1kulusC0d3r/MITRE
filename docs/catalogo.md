# Catálogo do ecossistema

[← Início](../README.md) · [Guia operacional](guia-operacional.md) · [Histórico e manutenção](historico-e-manutencao.md)

Revisão documental: **23/10/2026** (atualização incremental; entradas anteriores revistas em 22/10/2026). **75 entradas**, incluindo projetos, programas, padrões, ferramentas e publicações — não são 72 frameworks distintos. P1 = recomendação editorial para começar; P2 = aprofundamento por necessidade. A classificação não é ranking de mercado.

Cada nome aponta para uma fonte primária. Para Vulcan e eMASSer, o portal SAF é a referência de descoberta. Ter site ou repositório acessível não demonstra manutenção ativa, compatibilidade ou eficácia. Consulte o inventário JSON e as ressalvas de manutenção.

## Bases e modelos

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [ATT&CK](https://attack.mitre.org/) | MITRE | Descrever comportamentos adversários observados; Enterprise, Mobile e ICS. | Técnicas e procedimentos com evidência | P1 |
| [D3FEND](https://d3fend.mitre.org/) | MITRE | Relacionar contramedidas e artefatos digitais em uma ontologia defensiva. | Hipóteses de controles a validar | P1 |
| [Engage](https://engage.mitre.org/) | MITRE | Planejar deception, denial e engajamento de adversários. | Plano de engajamento com objetivos e limites | P1 |
| [ATLAS](https://atlas.mitre.org/) | MITRE | Modelar ameaças envolvendo sistemas de IA. | Cenários e técnicas de ameaça para IA | P1 |
| [EMB3D](https://emb3d.mitre.org/) | MITRE | Relacionar propriedades de dispositivos embarcados a ameaças e mitigações. | Modelo de ameaças de dispositivo | P1 |
| [ESTM](https://estm.mitre.org/) | MITRE | Explorar táticas e técnicas de ataques a sistemas embarcados. | Cenários para avaliação de sistemas embarcados | P2 |
| [FiGHT](https://fight.mitre.org/) | MITRE | Modelar ameaças ao ecossistema 5G. | Modelo de ameaças de telecomunicações | P2 |
| [CAPEC](https://capec.mitre.org/) | MITRE | Consultar padrões de ataque. | Padrões aplicáveis ao desenho do sistema | P2 |
| [CWE](https://cwe.mitre.org/) | MITRE | Classificar tipos de fraquezas de software e hardware. | Taxonomia de causas de vulnerabilidades | P2 |
| [CVE](https://www.cve.org/) | Programa CVE / ecossistema MITRE | Identificar vulnerabilidades publicamente divulgadas. | Identificadores e registros de vulnerabilidade | P2 |

## Detecção e validação

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [CAR](https://car.mitre.org/) | MITRE | Consultar hipóteses e analíticas explicadas com base em ATT&CK. | Pseudocódigo e requisitos de dados | P1 |
| [BZAR](https://github.com/mitre-attack/bzar) | MITRE | Analisar SMB/RPC com scripts Zeek orientados a comportamentos ATT&CK. | Referência de detecção de rede | P2 |
| [CALDERA](https://caldera.mitre.org/) | MITRE | Orquestrar emulação adversária em ambientes autorizados. | Evidência de exercícios e validação | P1 |
| [ATT&CK Evaluations](https://evals.mitre.org/) | MITRE | Examinar avaliações públicas e suas metodologias. | Evidência contextual de capacidade; não ranking universal | P2 |

## Automação e engenharia

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [SAF](https://saf.mitre.org/) | MITRE | Automatizar avaliação e normalização de resultados de segurança. | Resultados comparáveis de controles | P2 |
| [Heimdall](https://github.com/mitre/heimdall2) | MITRE | Visualizar e comparar resultados de avaliações. | Visão consolidada de conformidade | P2 |
| [SAF CLI](https://github.com/mitre/saf) | MITRE | Normalizar saídas de ferramentas e apoiar pipelines de segurança. | Dados normalizados e validações | P2 |
| [Vulcan](https://saf.mitre.org/) | MITRE | Criar e gerenciar orientação e baselines de segurança; acessar Apps → Vulcan. | Baseline de requisitos | P2 |
| [eMASSer](https://saf.mitre.org/) | MITRE | Integrar workflows de avaliação ao eMASS; acessar Apps → eMASSer. | Integração de resultados de avaliação | P2 |
| [CREF Navigator](https://crefnavigator.mitre.org/) | MITRE / referência NIST | Explorar relações de engenharia de resiliência cibernética. | Decisões arquiteturais de resiliência | P2 |

## CTI e formação

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [ECHO](https://www.mitre.org/news-insights/fact-sheet/enhanced-cti-sharing-partner-organizations) | MITRE | Conhecer aplicação de extração e contextualização de CTI. | Referência institucional; verificar acesso | P2 |
| [eCTF](https://ectf.mitre.org/) | MITRE | Praticar segurança de sistemas embarcados em competição. | Experiência de projeto e avaliação | P2 |
| [TTP-Based Hunting](https://www.mitre.org/news-insights/publication/ttp-based-hunting) | MITRE | Organizar hunting orientado a comportamentos. | Hipóteses e espaço de análise | P2 |
| [11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) | MITRE | Estudar desenho e evolução de um SOC. | Plano operacional e de maturidade | P2 |

## Cloud

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [CAVEaT](https://cloudsecurityalliance.org/artifacts/cloud-adversarial-vectors-exploits-and-threats) | CSA / colaboração MITRE | Estruturar ameaças e orientação de segurança para cloud. | Cenários cloud e requisitos defensivos | P2 |

## Dados e ferramentas ATT&CK

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Navigator](https://github.com/mitre-attack/attack-navigator) | MITRE | Visualizar e anotar matrizes. | Layers JSON para comunicar prioridade e evidência | P1 |
| [Workbench](https://github.com/mitre-attack/attack-workbench-frontend) | MITRE | Gerenciar extensões locais de ATT&CK. | Coleções locais e anotações | P1 |
| [ATT&CK STIX 2.1](https://github.com/mitre-attack/attack-stix-data) | MITRE | Consumir a base ATT&CK em formato estruturado. | Snapshots versionados de objetos e relações | P1 |
| [ATT&CK STIX 2.0](https://github.com/mitre/cti) | MITRE | Consultar a representação STIX 2.0. | Integração compatível com consumidores STIX 2.0 | P1 |
| [mitreattack-python](https://github.com/mitre-attack/mitreattack-python) | MITRE | Consultar e transformar dados ATT&CK com Python. | Consultas e exportações reproduzíveis | P1 |
| [ATT&CK Data Model](https://github.com/mitre-attack/attack-data-model) | MITRE | Validar e manipular dados ATT&CK com schemas TypeScript/Zod. | Validação estrutural | P1 |
| [Workbench TAXII Server](https://github.com/mitre-attack/attack-workbench-taxii-server) | MITRE | Servir coleções ATT&CK via TAXII. | Intercâmbio de CTI | P1 |
| [Workbench REST API](https://github.com/mitre-attack/attack-workbench-rest-api) | MITRE | Servir o back-end REST do Workbench para objetos e coleções ATT&CK. | API para integração e automação do Workbench | P2 |
| [Workbench Deployment](https://github.com/mitre-attack/attack-workbench-deployment) | MITRE | Implantar a pilha do Workbench (frontend, REST API, TAXII) com scripts prontos. | Ambiente Workbench reproduzível | P2 |
| [ATT&CK Website](https://github.com/mitre-attack/attack-website) | MITRE | Consultar o código-fonte do site oficial ATT&CK e a origem de suas páginas geradas. | Referência de como o conteúdo é publicado | P2 |

## CTID · Emulação

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library) | MITRE / CTID | Planejar emulações baseadas em TTPs documentadas. | Plano de exercício e evidências | P1 |

## CTID · CTI

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Attack Flow](https://github.com/center-for-threat-informed-defense/attack-flow) | MITRE / CTID | Representar sequência, condições e ramificações de ataques. | Fluxo de ataque comunicável | P1 |
| [TRAM](https://github.com/center-for-threat-informed-defense/tram) | MITRE / CTID | Apoiar mapeamento de relatórios de CTI para ATT&CK. | Sugestões de técnicas para revisão humana | P2 |
| [CTI Blueprints](https://github.com/center-for-threat-informed-defense/cti-blueprints) | MITRE / CTID | Estruturar relatórios de inteligência acionáveis. | Relatório com contexto e decisões | P1 |
| [Insider Threat TTP KB](https://github.com/center-for-threat-informed-defense/insider-threat-ttp-kb) | MITRE / CTID | Consultar comportamentos de ameaças internas. | Hipóteses de investigação contextualizadas | P2 |
| [ATT&CK Powered Suit](https://github.com/center-for-threat-informed-defense/attack-powered-suit) | MITRE / CTID | Consultar ATT&CK por extensão de navegador. | Apoio à análise de textos | P2 |
| [Technique Inference Engine](https://github.com/center-for-threat-informed-defense/technique-inference-engine) | MITRE / CTID | Inferir técnicas associadas a comportamentos observados. | Hipóteses; não fatos de inteligência | P2 |
| [Sightings Ecosystem](https://github.com/center-for-threat-informed-defense/sightings_ecosystem) | MITRE / CTID | Estudar observações e prevalência de técnicas. | Contexto empírico de priorização | P2 |

## CTID · Priorização

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Top ATT&CK Techniques](https://github.com/center-for-threat-informed-defense/top-attack-techniques) | MITRE / CTID | Priorizar técnicas usando o método e contexto do projeto. | Lista inicial de técnicas; adaptar ao ambiente | P1 |

## CTID · Mapeamentos

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Mappings Explorer](https://github.com/center-for-threat-informed-defense/mappings-explorer) | MITRE / CTID | Explorar relações entre controles e comportamentos ATT&CK. | Crosswalk documentado de capacidades | P1 |
| [Mappings Editor](https://github.com/center-for-threat-informed-defense/mappings-editor) | MITRE / CTID | Criar mapeamentos de capacidades para ATT&CK; beta na descrição consultada. | Mapeamentos com justificativa | P2 |

## CTID · Formação

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [CTID Public Resources](https://github.com/center-for-threat-informed-defense/public-resources) | MITRE / CTID | Localizar materiais públicos do Center. | Referências adicionais | P2 |
| [CTID Workshop](https://github.com/center-for-threat-informed-defense/workshop) | MITRE / CTID | Acessar materiais de workshops do Center. | Exercícios e material de estudo | P2 |

## CTID · Detecção

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Summiting the Pyramid](https://github.com/center-for-threat-informed-defense/summiting-the-pyramid) | MITRE / CTID | Avaliar robustez e qualidade de analíticas. | Avaliação de resistência à evasão | P1 |
| [Cloud Analytics](https://github.com/center-for-threat-informed-defense/cloud-analytics) | MITRE / CTID | Estudar analíticas comportamentais para cloud. | Blueprint e hipóteses de detecção | P2 |
| [Sensor Mappings to ATT&CK](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack) | MITRE / CTID | Relacionar sensores e eventos a comportamentos. | Plano de telemetria | P1 |
| [Ambiguous Techniques](https://ctid.mitre.org/projects/ambiguous-techniques/) | MITRE / CTID | Distinguir uso benigno de técnicas e contexto malicioso. | Enriquecimento e redução de ambiguidades | P1 |

## CTID · Fraude

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Fight Fraud Framework](https://github.com/center-for-threat-informed-defense/fight-fraud-framework) | MITRE / CTID | Estruturar análise comportamental de fraude financeira. | Cenários e hipóteses de fraude | P2 |

## CTID · Dados

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [ATT&CK Sync](https://github.com/center-for-threat-informed-defense/attack-sync) | MITRE / CTID | Apoiar adoção de mudanças entre versões ATT&CK. | Processo de atualização de bases | P2 |

## CTID · Modelagem

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Threat Modeling with ATT&CK](https://github.com/center-for-threat-informed-defense/threat-modeling-with-attack) | MITRE / CTID | Integrar ATT&CK a uma metodologia de threat modeling. | Modelo conectado a comportamentos adversários | P1 |

## CTID · OT

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Defending OT with ATT&CK](https://github.com/center-for-threat-informed-defense/defending-ot-with-attack) | MITRE / CTID | Adaptar coleções de ameaças a ambientes OT. | Coleção contextual para OT | P1 |

## CTID · Cloud

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [Defending IaaS with ATT&CK](https://github.com/center-for-threat-informed-defense/defending-iaas-with-attack) | MITRE / CTID | Selecionar técnicas relevantes para Linux IaaS. | Coleção de ameaças IaaS | P2 |

## CTID · Vulnerabilidades

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [CWE Calculator](https://github.com/center-for-threat-informed-defense/cwe-calculator) | MITRE / CTID | Apoiar priorização empírica de fraquezas. | Pontuação contextual de CWEs | P2 |

## CTID · Maturidade

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [INFORM](https://github.com/center-for-threat-informed-defense/inform) | MITRE / CTID | Avaliar adoção de defesa orientada por ameaças. | Diagnóstico e plano de evolução | P1 |

## Comunidade e fornecedores

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT) | Rabobank / comunidade | Pontuar qualidade de dados, visibilidade e detecção. | YAMLs e layers Navigator | P1 |
| [RE&CT](https://github.com/atc-project/atc-react) | ATC Project | Organizar ações e playbooks de resposta a incidentes. | Matriz de ações e playbooks revisados | P1 |
| [Sigma](https://github.com/SigmaHQ/sigma) | SigmaHQ | Representar e compartilhar regras de detecção. | Regras adaptadas e testadas no backend | P1 |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | Red Canary / comunidade | Validar comportamentos isolados em laboratório. | Resultados de testes por técnica | P1 |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | Filigran / comunidade | Organizar entidades e relações de inteligência. | Grafo de CTI com proveniência | P2 |
| [MISP Galaxy](https://github.com/MISP/misp-galaxy) | MISP Project | Contextualizar eventos com clusters de inteligência. | Enriquecimento e classificação | P2 |
| [Splunk Attack Range](https://github.com/splunk/attack_range) | Splunk | Montar ambiente instrumentado para exercícios. | Telemetria de laboratório | P2 |
| [Splunk Security Content](https://github.com/splunk/security_content) | Splunk | Estudar conteúdo de detecção e investigação. | Analíticas adaptadas para Splunk | P2 |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | Elastic | Estudar regras e workflows de detecção. | Analíticas adaptadas para Elastic | P2 |
| [Security Datasets](https://github.com/OTRF/Security-Datasets) | OTRF | Reproduzir eventos de segurança para pesquisa. | Dados para testes e replay | P2 |

## Padrões e referências complementares

| Projeto / fonte | Origem | Para que usar | Entrega esperada | Prioridade |
|---|---|---|---|:---:|
| [STIX](https://oasis-open.github.io/cti-documentation/) | OASIS | Representar inteligência estruturada. | Objetos e relações de CTI | P2 |
| [TAXII](https://oasis-open.github.io/cti-documentation/taxii/intro.html) | OASIS | Transportar e compartilhar CTI. | Coleções consumíveis por API | P2 |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | NIST | Organizar resultados de gestão de risco, incluindo Respond e Recover. | Perfil de resultados e responsabilidades | P2 |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | NIST | Integrar resposta a incidentes à gestão de risco. | Processos de resposta e melhoria contínua | P2 |
| [CVSS](https://www.first.org/standards/) | FIRST | Caracterizar severidade técnica de vulnerabilidades. | Vetor e pontuação de severidade | P2 |
| [EPSS](https://www.first.org/epss/) | FIRST | Estimar probabilidade de exploração para priorização. | Probabilidade estimada; combinar com exposição e impacto | P2 |

## Como não confundir os projetos

| Nome | Distinção necessária |
|---|---|
| D3FEND | Ontologia de contramedidas; não comprova a eficácia de um controle nem prescreve uma prioridade universal. |
| DeTT&CT | Projeto Rabobank/comunidade para cobertura e qualidade de dados; não é um framework oficial da MITRE. |
| RE&CT | Projeto ATC para ações de resposta; não é MITRE. Há sinais de baixa atualização: o campo `pushed_at` consultado indica 2022. |
| RESPOND | Nome de uma função do NIST CSF. Não foi confirmado um framework oficial MITRE com esse nome na pesquisa. Se houver outro projeto específico, exigir URL e mantenedor antes de classificar. |
| FiGHT / Fight Fraud Framework | FiGHT trata de 5G; Fight Fraud Framework trata de fraude financeira. Não são o mesmo projeto. |
| CVE / CWE / CAPEC / ATT&CK | Vulnerabilidade específica / tipo de fraqueza / padrão de ataque / comportamento adversário. Relações não são equivalências automáticas. |
| STIX / TAXII | Padrões hoje mantidos na OASIS; não apresentar como produtos atuais exclusivos da MITRE. |
| CVSS / EPSS | FIRST; severidade e probabilidade de exploração são dimensões diferentes. |
| CAR / ATT&CK Analytics | Bases relacionadas, mas com identidades e modelos próprios. Verificar versão e origem ao importar. |

## Dados ATT&CK e compatibilidade

A [página oficial de dados e ferramentas](https://attack.mitre.org/resources/attack-data-and-tools/) é a referência para STIX, TAXII, Excel e ferramentas. A navegação atual distingue **Detection Strategies, Analytics e Data Components**. Guias antigos centrados em Data Sources podem exigir adaptação. Fixe versão do ATT&CK, domínio, schema da ferramenta e commit dos dados; trate objetos revogados/depreciados explicitamente. Não assuma que um layer, YAML DeTT&CT ou consumidor STIX antigo aceita a base mais recente.

## Versão atual do ATT&CK

**ATT&CK v20** foi publicada em **13/10/2026** ([notas oficiais](https://attack.mitre.org/resources/updates/)). Destaques: técnicas Enterprise ligadas a IA (por exemplo, AI-Enabled Exfiltration e Direct/Indirect Prompt Injection), novas técnicas ICS de execução e comando e controle, Detection Strategies de ICS com contexto de plataforma e ativo, e Detection Strategies de Mobile que consideram os limites de visibilidade de Android e iOS. Totais informados: 971 Software, 182 Groups e 61 Campaigns. Ao migrar, fixe a versão e reveja layers, mapeamentos e consumidores STIX; para modelagem de IA, combine com ATLAS.

## Portais para expansão contínua

- [Recursos de cibersegurança da MITRE](https://www.mitre.org/focus-areas/cybersecurity/capabilities-resources)
- [Projetos CTID](https://ctid.mitre.org/projects/)
- [Organização MITRE](https://github.com/mitre)
- [Organização MITRE ATT&CK](https://github.com/mitre-attack)
- [Organização CTID](https://github.com/center-for-threat-informed-defense)

Este catálogo cobre o ecossistema de **cibersegurança e defesa orientada por ameaças**. Não pretende inventariar toda a produção institucional da MITRE em saúde, aviação, transporte e outras áreas. Plugins individuais, forks e cada regra de detecção ficam fora da contagem principal.

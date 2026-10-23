# 🧩 Cinco casos guiados

[← Início](../README.md) · [Guia operacional](../docs/guia-operacional.md)

| Caso | Tema | Tipo |
|:-:|---|---|
| 1 | [PowerShell fora do padrão](#caso-1--powershell-fora-do-padrão-operacional) | hipotético |
| 2 | [Embarcado em OT](#caso-2--ameaça-a-dispositivo-embarcado-em-ot) | hipotético |
| 3 | [IA com recuperação de documentos](#caso-3--abuso-de-sistema-de-ia-com-recuperação-de-documentos) | hipotético |
| 4 | [Migrar regras para o ATT&CK v20](#caso-4--migrar-regras-de-detecção-para-o-attck-v20) | **executado em 22/10/2026** |
| 5 | [Fraude via Pix e mobile banking](#caso-5--fraude-via-pix-e-mobile-banking) | hipotético |

**Os casos 1, 2, 3 e 5 são exemplos didáticos hipotéticos.** Não representam incidentes investigados ou testes executados; os resultados são critérios de aceite propostos. O caso 4 foi executado com dados públicos nesta revisão e traz os números obtidos.

## Caso 1 — PowerShell fora do padrão operacional

**Contexto:** endpoints Windows de uma equipe financeira; scripts administrativos legítimos já existem.

**Pergunta:** conseguimos distinguir uma execução suspeita de uma automação conhecida e entregar contexto suficiente à triagem?

| Etapa | Trabalho | Entrega |
|---|---|---|
| Modelagem | Consultar [T1059.001](https://attack.mitre.org/techniques/T1059/001/) e registrar o procedimento específico | Mapeamento justificado; não marcar toda T1059 como coberta |
| Telemetria | Verificar processos, comandos e logs PowerShell disponíveis; sensibilidade dos dados e retenção | Contrato de coleta com campos e limitações |
| Detecção | Consultar CAR/Sigma; correlacionar origem, processo pai, identidade e padrão local | Regra específica para o ambiente |
| Qualidade | Aplicar Summiting e considerar explicações benignas | Avaliação de robustez e hipóteses de falso positivo |
| Validação | Selecionar teste Atomic autorizado, revisar pré-requisitos e limpeza | Evidência de evento → alerta → triagem |
| Resposta | Documentar coleta, investigação e decisão de contenção com RE&CT | Playbook com dono e reversão |

**Critério de aceite proposto:** o procedimento escolhido gera os campos previstos e o alerta dentro da meta definida pela equipe; uma automação administrativa conhecida é corretamente contextualizada. Falha em qualquer etapa vira uma lacuna específica.

**Não concluir:** detectar um comando de teste significa detectar todo abuso de PowerShell.

## Caso 2 — Ameaça a dispositivo embarcado em OT

**Contexto:** gateway entre rede de supervisão e dispositivos industriais. Disponibilidade e segurança do processo restringem mudanças e ensaios.

**Pergunta:** quais propriedades do gateway permitem cenários de comprometimento e que controles podem ser avaliados sem afetar o processo?

| Etapa | Trabalho | Entrega |
|---|---|---|
| Contexto | Inventariar interfaces, firmware, manutenção remota e fronteiras | Diagrama e propriedades confirmadas |
| Modelagem | Consultar [EMB3D](https://emb3d.mitre.org/) e [ESTM](https://estm.mitre.org/); selecionar ameaças sustentadas pelas propriedades | Modelo de ameaças do dispositivo |
| Operação | Consultar [ATT&CK ICS](https://attack.mitre.org/matrices/ics/) e Defending OT | Cenário operacional; IDs só após confirmar comportamento |
| Defesa | Usar D3FEND para descrever capacidades e avaliar viabilidade de aplicação | Controles candidatos com restrições |
| Telemetria | Priorizar observação passiva, logs de gestão e integridade quando disponíveis | Plano de visibilidade sem prometer cobertura inexistente |
| Validação | Começar por replay de dados e exercício de mesa; ensaio técnico em laboratório | Evidências e limitações explícitas |
| Resposta | Planejar decisão conjunta com operação e recuperação validada pelo responsável | Playbook sem isolamento automático indiscriminado |

**Critério de aceite proposto:** cada ameaça selecionada possui propriedade de origem, evidência, controle candidato, forma de teste e responsável operacional. Não confundir ATT&CK ICS com cobertura de todo componente embarcado.

## Caso 3 — Abuso de sistema de IA com recuperação de documentos

**Contexto:** assistente corporativo consulta documentos internos e pode acionar ferramentas com permissões delimitadas.

**Pergunta:** conteúdo recuperado consegue induzir comportamento indevido ou acesso além do escopo da identidade?

| Etapa | Trabalho | Entrega |
|---|---|---|
| Escopo | Mapear entrada, índice, documentos, modelo, ferramentas e identidades | Fluxo de dados e fronteiras de confiança |
| Modelagem | Consultar [ATLAS](https://atlas.mitre.org/) para localizar técnicas e casos realmente aplicáveis | Cenário de abuso com evidência da correspondência |
| Defesa | Definir autorização nas ferramentas, isolamento e validações de saída conforme arquitetura | Requisitos verificáveis; não depender só de prompt |
| Telemetria | Registrar origem do documento, decisões de autorização e chamadas de ferramenta com minimização de dados | Trilhas de auditoria correlacionáveis |
| Teste | Usar documentos sintéticos e ferramentas simuladas em ambiente de teste | Conjunto de casos benignos e adversariais |
| Resposta | Revogar acesso indevido, preservar evidência e revalidar comportamento após correção | Playbook e testes de regressão |

**Critério de aceite proposto:** casos definidos não ultrapassam permissões e deixam evidência auditável; falhas são reproduzíveis e alimentam correção. Não aplicar a matriz Enterprise mecanicamente a ameaças específicas de IA nem considerar filtragem de prompt uma garantia de segurança.

## Caso 4 — Migrar regras de detecção para o ATT&CK v20

**Tipo:** executado em 22/10/2026 com dados públicos (ATT&CK 18.1 e 20.0, SigmaHQ `main`, Atomic Red Team `master`, CAPEC 3.9).

**Pergunta:** depois da divisão de Defense Evasion, quais regras citam IDs que não existem mais, e para onde movê-las?

| Etapa | Comando | Resultado obtido |
|---|---|---|
| Baixar versões fixas | `./scripts/fetch_all.sh` | bundles 20.0 com SHA-256 no manifesto |
| Ver o que saiu | `python3 scripts/attack_diff.py 18.1 20.0` | 1 tática nova (TA0112), 1 renomeada (TA0005 → Stealth), 32 técnicas novas ou reativadas, 17 revogadas, 4 renomeadas |
| Cruzar com regras | `python3 scripts/attack_diff.py 18.1 20.0 --rules sigma/rules` | 55 ocorrências de IDs revogados no SigmaHQ (ex.: `lnx_auditd_disable_system_firewall.yml` cita T1562.004 → T1686) |
| Medir material disponível | `coverage_layer.py` em Sigma e Atomic, depois `--merge` | Sigma cita 407 técnicas; Atomic tem 346; 277 nos dois; 130 só com regra; 69 só com teste |
| Checar crosswalk de vulnerabilidade | `python3 scripts/capec_xwalk.py --stale-only` | 15 mapeamentos CAPEC → ATT&CK obsoletos (ex.: CAPEC-268 → T1562.002, substituta T1685.001) |

**Entregas no repositório:** [`crosswalks/attack-v18.1-v20.0-substituicoes.tsv`](../crosswalks/attack-v18.1-v20.0-substituicoes.tsv), [`crosswalks/cwe-capec-attack.tsv`](../crosswalks/cwe-capec-attack.tsv) e as camadas em [`layers/`](../layers).

**Limites:** contagem de artefatos que **citam** uma técnica não é cobertura de detecção. Uma técnica revogada com substituta declarada ainda exige revisão humana: T1562.001 e T1562.006 foram ambas para T1685, mas a regra pode caber melhor numa subtécnica.

**Para o seu time:** troque `sigma/rules` pela pasta das regras da casa (Sigma, SPL, KQL, YARA-L) e anexe a saída ao ticket de migração.

## Caso 5 — Fraude via Pix e mobile banking

**Contexto:** cliente financeiro com app mobile; golpes com engenharia social, contas laranja e automação contra CAPTCHA no onboarding.

**Pergunta:** quais comportamentos conseguimos observar entre o primeiro contato com a vítima e a transferência, e quem age em cada ponto?

| Etapa | Trabalho | Entrega |
|---|---|---|
| Modelagem | Combinar [Fight Fraud Framework](https://github.com/center-for-threat-informed-defense/fight-fraud-framework) (etapas da fraude), [ATT&CK Mobile](https://attack.mitre.org/matrices/mobile/) e técnicas Enterprise como T1684 Social Engineering e T1696 Anti-Automation Evasion | Cenário ponta a ponta com evidência por etapa |
| Telemetria | Listar sinais do app (dispositivo, sessão, biometria comportamental), antifraude e canal de atendimento | Contrato de telemetria entre segurança e antifraude |
| Detecção | Hipóteses por etapa: novo dispositivo + alteração de chave Pix + transferência atípica; volume anômalo de CAPTCHA resolvido | Regras com donos de cada área |
| Resposta | Bloqueio cautelar, contato com o cliente, preservação de evidência e comunicação ao banco recebedor conforme as regras do Pix | Playbook com prazos e responsáveis |
| Validação | Exercício de mesa com antifraude, SOC e atendimento | Lacunas de integração entre times |

**Critério de aceite proposto:** cada etapa do cenário tem ao menos um sinal, um dono e uma decisão definida. **Não concluir:** que técnicas ATT&CK sozinhas descrevem fraude; o F3 existe porque a cadeia financeira tem etapas próprias.

## Como evoluir os casos

Preencha o [template](../templates/caso-operacional.md), fixe as versões das fontes e substitua cada hipótese por observação quando houver evidência. Adicione resultados reais somente com escopo, data, ambiente, procedimento, dados e limitações.

# Três casos guiados

[← Início](../README.md) · [Guia operacional](../docs/guia-operacional.md)

**Exemplos didáticos hipotéticos. Não representam incidentes investigados ou testes executados.** Os resultados abaixo são critérios de aceite propostos, não resultados obtidos.

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

## Como evoluir os casos

Preencha o [template](../templates/caso-operacional.md), fixe as versões das fontes e substitua cada hipótese por observação quando houver evidência. Adicione resultados reais somente com escopo, data, ambiente, procedimento, dados e limitações.

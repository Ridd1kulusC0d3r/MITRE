# Guia operacional: do contexto à evidência

[← Início](../README.md) · [Catálogo](catalogo.md) · [Casos](../examples/casos-guiados.md)

Este fluxo é uma proposta editorial de composição dos recursos. Não é um novo framework oficial MITRE e não pressupõe integrações prontas.

## 1. Defina o problema antes da técnica

Registre processo de negócio, ativos, identidades, fronteiras de confiança, exposição e impacto. Uma técnica frequente globalmente pode não ser prioritária no seu ambiente.

**Saída:** escopo e pergunta de inteligência. Exemplo: “Conseguimos identificar execução não usual de PowerShell nos endpoints financeiros e preservar evidências antes da contenção?”

**Fontes:** [Threat Modeling with ATT&CK](https://github.com/center-for-threat-informed-defense/threat-modeling-with-attack), [Top ATT&CK Techniques](https://github.com/center-for-threat-informed-defense/top-attack-techniques).

## 2. Modele o comportamento e preserve a proveniência

Extraia procedimentos de relatórios ou evidências locais. Relacione técnica/subtécnica somente quando a descrição sustentar o comportamento. Identifique observação, hipótese e inferência separadamente. TRAM e TIE apoiam análise, mas seus resultados precisam de revisão.

**Saída:** tabela de evidências com URL, trecho ou localização, data, confiança e justificativa do mapeamento. Use Attack Flow quando ordem, condições e ramificações importarem.

**Fontes:** [ATT&CK](https://attack.mitre.org/), [Attack Flow](https://github.com/center-for-threat-informed-defense/attack-flow), [CTI Blueprints](https://github.com/center-for-threat-informed-defense/cti-blueprints).

## 3. Transforme comportamento em requisitos observáveis

Defina evento, sensor, campos, cobertura de ativos, retenção, latência e integridade da coleta. “Temos EDR” não informa quais eventos estão disponíveis.

**Saída:** contrato de telemetria. Exemplo: processo pai, executável, linha de comando, usuário, host e horário; explicitar os campos ausentes e o que deixam de permitir.

Use Sensor Mappings como referência e DeTT&CT para registrar avaliações. **Visibilidade é possibilidade de observar; detecção é lógica implementada e avaliada.** Não copiar pontuações sem evidência.

**Fontes:** [Sensor Mappings](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack), [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT).

## 4. Escreva a hipótese e a analítica

Descreva o comportamento suspeito, o contexto que o torna suspeito e as explicações benignas. Estude CAR, Detection Strategies/Analytics do ATT&CK e regras Sigma, Splunk ou Elastic conforme o backend.

**Saída:** regra versionada, dependências de dados, exceções justificadas e procedimento de triagem. Um ID ATT&CK na regra não demonstra que todas as implementações da técnica são detectadas.

Use Summiting the Pyramid para avaliar robustez; use Ambiguous Techniques para orientar distinções entre comportamentos legítimos e maliciosos.

**Fontes:** [CAR](https://car.mitre.org/), [dados ATT&CK](https://attack.mitre.org/resources/attack-data-and-tools/), [Summiting](https://github.com/center-for-threat-informed-defense/summiting-the-pyramid), [Ambiguous Techniques](https://ctid.mitre.org/projects/ambiguous-techniques/).

## 5. Selecione contramedidas e planeje a resposta

D3FEND ajuda a nomear capacidades defensivas; Mappings Explorer ajuda a relacionar controles a comportamentos. As relações são pontos de investigação, não prova de bloqueio.

Para resposta, registre gatilho, responsável, evidência a preservar, decisão, ação, reversão e recuperação. RE&CT fornece uma taxonomia útil, mas seu conteúdo deve ser revisado contra ambiente e orientações atuais. Engage entra quando houver um objetivo específico de deception e capacidade de operar o plano.

**Saída:** controle com hipótese de eficácia + playbook operacional.

**Fontes:** [D3FEND FAQ](https://d3fend.mitre.org/faq/), [Mappings Explorer](https://github.com/center-for-threat-informed-defense/mappings-explorer), [RE&CT](https://github.com/atc-project/atc-react), [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

## 6. Valide por procedimento, não apenas por técnica

Escolha teste isolado com Atomic Red Team ou campanha com CALDERA/Adversary Emulation Library. Defina ambiente autorizado, pré-condições, comportamento esperado, limpeza e critérios de interrupção.

**Saída:** registro de execução, eventos brutos, resultado da regra, tempo até alerta, triagem e resultado da resposta. Inclua teste benigno de contraste. Separar falha de coleta, falha da regra, falha de integração e falha operacional.

Em OT, comece com replay e exercício de mesa; qualquer ensaio ativo precisa de laboratório e validação operacional apropriada.

**Fontes:** [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), [CALDERA](https://caldera.mitre.org/), [Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library).

## 7. Publique o resultado e trate as lacunas

Use Navigator para comunicar a situação; o score deve ter legenda e evidência rastreável. Registre versão ATT&CK, data do teste, plataformas cobertas e restrições. Use INFORM para conectar lacunas técnicas a evolução do programa.

**Saída:** backlog priorizado com dono, prazo, dependência e critério de aceite.

## Métricas que ajudam

| Métrica | Como calcular ou registrar | Limitação |
|---|---|---|
| Cobertura de telemetria | Ativos no escopo com campos necessários / ativos no escopo | Não prova detecção |
| Sucesso no conjunto de testes | Procedimentos detectados / procedimentos válidos executados | Só representa a amostra testada |
| Tempo até alerta | Horário do alerta − horário do comportamento | Separar atraso de ingestão |
| Ruído | Alertas benignos revisados / alertas revisados, com janela e amostra | Depende da qualidade da triagem |
| Resposta validada | Cenários com ações e recuperação exercitadas / cenários selecionados | Exercício de mesa não equivale a execução técnica |
| Robustez | Resultado documentado da avaliação Summiting | Não substituir por score inventado |
| Drift | Mudanças de dados, regras, ativos ou versões desde o último teste | Exige novo teste quando a hipótese mudar |

## Entrega mínima e entrega completa

**Mínima:** cenário, evidência, técnica justificada, requisito de telemetria, hipótese de detecção, teste e responsável pela resposta.

**Completa:** acrescente Attack Flow, avaliação de qualidade DeTT&CT, contramedidas D3FEND, avaliação Summiting, playbook, testes negativos, layer Navigator e plano de evolução INFORM.

Use o [template](../templates/caso-operacional.md) para manter a cadeia de rastreabilidade.

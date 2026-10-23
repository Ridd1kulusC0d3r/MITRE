# Novas referências — 23/10/2026

[← Início](../README.md) · [Catálogo](catalogo.md)

**12 adições sem duplicar as 114 entradas já presentes: o catálogo passa a 126.** “Novas” significa novas nesta curadoria, não necessariamente recém-lançadas. Referências antigas úteis foram marcadas com limitações.

## Onde estas adições ajudam

| Recurso | Lacuna que preenche | Como começar |
|---|---|---|
| [Dettectinator](https://github.com/siriussecurity/dettectinator) | Atualização manual dos YAMLs DeTT&CT | Importar um conjunto pequeno de regras e revisar cada técnica atribuída |
| [OpenAEV](https://github.com/OpenAEV-Platform/openaev) | Gestão de campanhas e exercícios conectados à CTI | Modelar um cenário, responsáveis e resultado esperado |
| [Threatest](https://github.com/DataDog/threatest) | Teste sem comprovação de que gerou o alerta esperado | Definir matcher, correlação e tempo limite para um procedimento |
| [TTPForge](https://github.com/facebookincubator/TTPForge) | Procedimentos de teste pouco repetíveis | Versionar uma simulação YAML com pré-condições e limpeza |
| [Splunk Attack Data](https://github.com/splunk/attack_data) | Falta de dados para desenvolver uma analítica | Selecionar um dataset e conferir contexto, campos e timestamps |
| [Elastic Protections Artifacts](https://github.com/elastic/protections-artifacts) | Pesquisa restrita às regras SIEM | Comparar lógica de endpoint e dependências de dados |
| [AWS Customer Playbook Framework](https://github.com/aws-samples/aws-customer-playbook-framework) | Resposta cloud genérica demais | Adaptar um playbook a contas, permissões e responsáveis |
| [ATLAS Arsenal](https://github.com/mitre-atlas/arsenal) | Falta de exemplos de emulação de ML | Estudar cenários; revisar dependências antigas antes de instalar |
| [BRAWL public game 001](https://github.com/mitre/brawl-public-game-001) | Falta de corpus de exercício para pesquisa | Avaliar os dados históricos e seus limites de representatividade |
| [D3FEND Extractors](https://d3fend.mitre.org/tools/) | Extração manual de referências técnicas em texto | Usar um texto público e revisar associações sugeridas |
| [D3TECT](https://ucrisportal.univie.ac.at/en/publications/strategic-selection-of-data-sources-for-cyber-attack-detection-in/) | Escolha de logs sem critérios de valor e restrição | Ler o modelo para estruturar a justificativa de telemetria |
| [Red Team Redemption](https://arxiv.org/abs/2408.15645) | Escolha de emulador baseada só em popularidade | Usar os critérios do estudo para construir um benchmark local |

## Prioridade editorial para engenharia de detecção

Minha sequência sugerida é **Dettectinator → Splunk Attack Data → Threatest**, usando TTPForge quando houver necessidade de procedimentos próprios e OpenAEV quando o problema passar a ser gestão de campanhas.

Essa sequência é uma proposta de trabalho, não uma integração pronta: as ferramentas usam formatos e backends diferentes. Não há garantia de importação direta entre elas.

Um primeiro caso pode entregar:
1. Inventário de uma detecção, com técnica justificada e dados necessários.
2. Replay de dataset em ambiente isolado para verificar parsing e lógica.
3. Teste de ponta a ponta que relacione execução e alerta.
4. Registro de lacuna: coleta, campos, regra, tempo de alerta ou resposta.
5. Atualização do mapa de cobertura com a evidência, evitando pontuação baseada só em tags.

## Distinções que evitam erros

- **OpenAEV é o nome atual de OpenBAS**, conforme [anúncio da Filigran](https://filigran.io/press-releases/filigran-redefines-proactive-security-openbas-rebrands-to-openaev-with-an-ai-powered-enterprise-edition). Não contar os dois como produtos independentes.
- **D3TECT é pesquisa acadêmica de seleção de fontes**, não outra grafia de DeTT&CT.
- **ATLAS Arsenal e ATT&CK Arsenal são projetos diferentes**. O primeiro é um plugin voltado a ML; a documentação consultada é antiga.
- **Splunk Attack Data, Attack Range e Security Content** entregam dados, ambiente e conteúdo analítico, respectivamente.
- **Elastic Protections Artifacts** complementa o repositório de regras de detecção com artefatos de endpoint. O README declara Elastic License 2.0.
- **BRAWL é incluído como dataset histórico**. A idade não elimina seu valor para pesquisa, mas impede tratá-lo como representação de ameaças atuais.
- **Extratores D3FEND** produzem relações candidatas; não substituem análise de contexto.

## Verificação e limites

Foram consultados READMEs, páginas dos mantenedores, registros acadêmicos e metadados GitHub. Não instalamos nem executamos essas ferramentas. Para os dois artigos, a análise se limitou ao resumo e registro bibliográfico; não foi uma revisão integral nem reprodução dos experimentos.

Os status de atividade são sinais editoriais: pushes recentes não comprovam qualidade ou suporte. OpenAEV distingue Community e Enterprise; avaliar recursos e termos de cada edição. Relações do inventário indicam composição conceitual, salvo integração expressamente descrita pelo mantenedor.

Os IDs adicionados são **E118–E129**. A data individual das 114 entradas anteriores foi preservada.


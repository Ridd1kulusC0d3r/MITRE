# Atualização — 11/11/2026

[← Início](../README.md) · [Catálogo](catalogo.md) · [Novidades 2026](novidades-2026.md)

**O catálogo passa de 126 para 131 entradas.** Nenhum repositório novo apareceu na organização `mitre-attack` (seguem 21); as novidades estão em versões e em projetos vizinhos da MITRE.

## O que mudou nas fontes

| Item | Antes | Agora | O que fazer |
|---|---|---|---|
| ATT&CK | v20.0 · 13/10/2026 | **v20.1 · 05/11/2026** | Nada nas regras: o diff de técnicas é vazio. Atualize o bundle fixado. |
| mitreattack-python | 6.3.1 | **6.4.0 · 05/11/2026** | Atualizar junto com o bundle |
| ATLAS | 2026.09 | **2026.10 · 28/10/2026** | Revisar mapeamentos por ID: há renomeações e subtécnicas movidas |
| Workbench · REST API | v4.18.0-alpha.1 · v4.26.0-alpha.1 | **v4.18.0 · v4.26.0** | Sair das tags alpha |
| pySigma · sigma-cli | 2.0.1 · 3.1.0 | **2.1.0 · 4.0.0** | sigma-cli mudou de versão principal: testar pipelines antes |
| Stratus Red Team | v2.37.1 | **v2.38.0** | — |
| Hayabusa | v4.2.0 | **v4.4.0** | — |
| CTID | "CIS Controls (out)" | **CIS Controls for Threat Mitigations · 05/10/2026** | Disponível no Mappings Explorer |

Os scripts deste repositório agora usam ATT&CK 20.1 e ATLAS 2026.10 por padrão. O arquivo `crosswalks/attack-v18.1-v20.0-substituicoes.tsv` continua válido para a v20.1.

## Cinco entradas novas

| Recurso | Para quê | Cuidado |
|---|---|---|
| [Caldera MCP](https://github.com/mitre/mcp) `E130` | Operar o Caldera por conversa: criar abilities, converter relatórios em STIX e planejar emulação | Conteúdo gerado por LLM; revisar antes de executar |
| [Caldera for OT](https://github.com/mitre/caldera-ot) `E131` | Plugins de protocolo industrial para o Caldera, alinhados ao ATT&CK for ICS | Só em laboratório isolado e autorizado |
| [Hipcheck](https://github.com/mitre/hipcheck) `E132` | Triar dependências de código aberto por risco de cadeia de suprimentos | Heurística; não substitui SCA |
| [Grid Watch](https://github.com/mitre/grid-watch) `E133` | Outstation DNP3 simulada, alvo de laboratório para o Caldera for OT | Simulação simplificada |
| [ATLAS Agent](https://github.com/mitre-atlas/atlas-knowledge-base-agent) `E134` | Consultar o ATLAS em linguagem natural, com servidor MCP e API | Dados embutidos da v2026.7, anteriores às mudanças da 2026.10 |

"Novas" significa novas nesta curadoria. Nenhuma foi instalada nem executada.

## Verificação

- ATT&CK: `index.json` do attack-stix-data e comparação dos bundles 20.0 e 20.1 dos três domínios com `scripts/attack_diff.py`.
- ATLAS: CHANGELOG do atlas-data e existência de `dist/v6/ATLAS-2026.10.yaml`.
- Versões: tags Git (`git ls-remote`) e PyPI.
- Entradas novas: README e arquivo LICENSE de cada repositório.
- Organizações `mitre-attack`, `mitre-atlas` e `center-for-threat-informed-defense`: listagens públicas do GitHub; a do CTID foi lida só na primeira página (30 de 31 repositórios).

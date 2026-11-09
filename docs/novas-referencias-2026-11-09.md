# Novas referências — 09/11/2026

[← Início](../README.md) · [Catálogo](catalogo.md)

Varredura de `attack.mitre.org`, das organizações `mitre-attack`, `center-for-threat-informed-defense` e `mitre` no GitHub (busca da API, 09/11/2026).

## Resultado

- **mitre-attack:** nenhum repositório novo; todos os ativos já estavam no catálogo (`attack-navigator`, `mitreattack-python`, `attack-stix-data`, `attack-workbench-*`, `attack-data-model`, `car`, `bzar`).
- **CTID:** nenhum repositório novo desde 23/10; `attack-flow` teve push em 27/10.
- **ATT&CK:** v20 (13/10/2026); o site cita conteúdo v20.1.
- **Organização `mitre`:** 4 adições relevantes (abaixo).

| Recurso | Para que serve | Cuidado |
|---|---|---|
| [Caldera MCP](https://github.com/mitre/mcp) | Plugin Caldera que usa LLM (e RAG com CTI em STIX) para gerar abilities e planejar operações | Não é Model Context Protocol; revisar o que o LLM gera antes de executar |
| [Caldera for OT](https://github.com/mitre/caldera-ot) | Plugins de emulação OT (`modbus`, `dnp3`, `bacnet`) | Só em laboratório isolado e autorizado |
| [Hipcheck](https://github.com/mitre/hipcheck) | Pontuação de risco de cadeia de suprimentos de repositórios | Heurística; não substitui SCA |
| [Grid Watch](https://github.com/mitre/grid-watch) | Sandbox DNP3 de rede elétrica | Projeto recente, uso externo incerto |

Metadados vieram da API; README e execução não foram verificados. Catálogo: 130 entradas.

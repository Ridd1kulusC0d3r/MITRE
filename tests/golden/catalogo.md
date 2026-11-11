<!-- ARQUIVO GERADO por python3 -m atlas build a partir de data/ecosystem.json. Não edite à mão. -->

# 🗺️ Catálogo do ecossistema

[← Início](../README.md) · [Explorador interativo](../index.html) · [Crosswalks](crosswalks.md) · [Novidades 2026](novidades-2026.md) · [Histórico](historico-e-manutencao.md)

Revisão: **2026-11-02** · **4 entradas** (frameworks, ferramentas, dados, padrões e publicações). P1 = comece aqui; P2 = aprofunde por necessidade. Não é ranking de mercado.

**Legenda.** Origem: 🟦 MITRE oficial · 🟩 MITRE CTID · 🟪 Colaboração MITRE · 🟫 Fundação aberta (código MITRE doado) · ⬛ Governo · ⬜ Organismo de padrão · 🟨 Comunidade · 🟧 Fornecedor · ◻️ Outro  
Status: ✅ Ativo · ⏸️ Baixa atividade · 🧊 Parado · ❔ Não verificado

## Índice por camada

| Camada | Pergunta | Itens |
|---|---|:---:|
| 🎯 [adversario](#adversario) | O que o adversário faz | 2 |
| 🛡️ [defesa](#defesa) | Como reduzir exposição | 1 |
| 🧪 [validacao](#validacao) | Como validar | 1 |

<a id="adversario"></a>
## 🎯 O que o adversário faz

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[ATLAS](https://atlas.mitre.org/)** `E004` | 🟦 MITRE | Modelar ameaças contra sistemas de IA e agentes: prompt injection, jailbreak, envenenamento de dados e abuso de ferramentas. | v2026.10 · 28/10/2026 | IA | P1 |
| ✅ | **[ATT&CK](https://attack.mitre.org/)** `E001` | 🟦 MITRE | Descrever comportamentos adversários observados; Enterprise, Mobile e ICS. | v20.1 · 05/11/2026 (v20.0 em 13/10/2026) | Enterprise, Mobile, ICS/OT, IA | P1 |

<details><summary>Notas e relações</summary>

- **ATLAS** — entrega: Cenários e técnicas de ameaça para IA. 16 táticas, 129 técnicas, 92 subtécnicas, 44 mitigações, 77 estudos de caso, 44 entidades e 37 softwares (CHANGELOG oficial). A 2026.10 renomeou AML.T0010 para Supply Chain Compromise e AML.T0005 para Replicate AI Model Behavior, e moveu subtécnicas de AML.T0024 para AML.T0137: revise mapeamentos por ID. Use dist/ATLAS-latest.yaml; dist/ATLAS.yaml foi depreciado. ↔ ATT&CK.
- **ATT&CK** — entrega: Técnicas e procedimentos com evidência. v19 dividiu Defense Evasion em Stealth (TA0005) e Defense Impairment (TA0112); v20 trouxe técnicas de IA (prompt injection direta e indireta T1699/T1698, AI-Enabled Exfiltration T1700) e anti-automação (T1696). Enterprise v20.1: 227 técnicas, 479 subtécnicas, 706 Detection Strategies, 1.773 Analytics. A v20.1 (05/11/2026) é correção de dados: nenhuma técnica entrou, saiu ou mudou de nome em Enterprise, Mobile ou ICS. Seções do site: Matrices, Tactics, Techniques, Mitigations, Assets (ICS), Detection Strategies, Analytics, Data Components, Groups, Software e Campaigns. ↔ D3FEND.

</details>

<a id="defesa"></a>
## 🛡️ Como reduzir exposição

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[D3FEND](https://d3fend.mitre.org/)** `E002` | 🟦 MITRE | Relacionar contramedidas e artefatos digitais em uma ontologia defensiva. | ontologia 1.6.0 · 31/08/2026 | Enterprise, ICS/OT, Espaço | P1 |

<details><summary>Notas e relações</summary>

- **D3FEND** — entrega: Hipóteses de controles a validar. 1.5.0 atualizou para ATT&CK v19.0 e mapeou ICS T0800–T0895. Issue #709: mapeamentos ainda citam técnicas revogadas na v19; validar contra a v20. ↔ ATT&CK.

</details>

<a id="validacao"></a>
## 🧪 Como validar

| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |
|:-:|---|---|---|---|---|:-:|
| ✅ | **[Apache Caldera](https://caldera.apache.org/)** `E013` | 🟫 Apache Software Foundation (código originado na MITRE) | Orquestrar emulação adversária em ambientes autorizados. | 5.3.0 (tag) | Enterprise, ICS/OT | P1 |

<details><summary>Notas e relações</summary>

- **Apache Caldera** — entrega: Evidência de exercícios e validação. Doado à Apache Software Foundation: Apache Caldera (Incubating), repo apache/caldera. ↔ ATT&CK, D3FEND.

</details>

## 🗄️ Itens históricos e depreciados

| Item | Situação |
|---|---|
| [attack-control-framework-mappings](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings) | Mapeamentos NIST migraram para Mappings Explorer, conforme descrição do repositório. |
| [security-stack-mappings](https://github.com/center-for-threat-informed-defense/security-stack-mappings) | Mapeamentos de stacks migraram para Mappings Explorer, conforme descrição do repositório. |

---

_Limites da verificação:_ Pesquisa documental; ferramentas não executadas. Campos ausentes: não coletados. archived=false não comprova manutenção ativa. pushed_at não equivale a último release. license_api não substitui leitura da licença. Status 'n/v' = não verificado. Tag Git indica marco publicado, não necessariamente release estável.

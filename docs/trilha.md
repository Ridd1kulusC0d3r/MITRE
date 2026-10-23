<!-- ARQUIVO GERADO por scripts/build_catalog.py a partir de data/trilha.json. Não edite à mão. -->

# 🧗 Trilha de 8 semanas: do ATT&CK à defesa validada

[← Início](../README.md) · [Versão interativa (uma ação por vez)](../index.html#trilha) · [Catálogo](catalogo.md)

> Uma ação por vez. Cada ação termina em algo que dá para mostrar. Marque a caixa, faça a próxima. No explorador, o progresso fica salvo no seu navegador.

| Semana | Tema | Entrega |
|:-:|---|---|
| 1 | [Fundamentos do ATT&CK v20](#semana-1) | Camada Navigator com grupos que miram o Brasil e a LATAM |
| 2 | [Dados, versões e migração](#semana-2) | Relatório das suas regras que citam técnicas revogadas |
| 3 | [Telemetria antes da regra](#semana-3) | Contrato de telemetria para 3 técnicas |
| 4 | [Detecção e robustez](#semana-4) | Uma regra Sigma convertida, versionada e avaliada |
| 5 | [Validação purple](#semana-5) | Evidência evento → alerta → triagem |
| 6 | [Defesa, resposta e forense](#semana-6) | Playbook ATT&CK → D3FEND → RE&CT para uma técnica crítica |
| 7 | [Vulnerabilidade como comportamento](#semana-7) | Fila de correção priorizada por técnica |
| 8 | [CTI avançada e domínios especiais](#semana-8) | Attack Flow de um relatório real + plano INFORM |

<a id="semana-1"></a>
## Semana 1 · Fundamentos do ATT&CK v20

**Entrega:** Camada Navigator com grupos que miram o Brasil e a LATAM

- [ ] **1.1** Leia a página de uma técnica que você já detecta (ex.: T1059.001) e anote procedimento, Detection Strategy e mitigação. — [ATT&CK](https://attack.mitre.org/), [ATT&CK Detection Strategies e Analytics](https://attack.mitre.org/detectionstrategies/)
- [ ] **1.2** Rode scripts/fetch_all.sh e confira o manifesto com SHA-256.
  ```bash
  ./scripts/fetch_all.sh
  ```
- [ ] **1.3** Gere a lista de técnicas por tática e conte quantas estão em Defense Impairment.
  ```bash
  python3 scripts/attack_dump.py --file data/cache/enterprise-attack-20.0.json > tecnicas.md
  ```
- [ ] **1.4** Liste as técnicas de 3 grupos com atuação na América Latina (ex.: Malteiro, APT-C-36, Machete, FIN13) com jq.
  ```bash
  ./scripts/jq-receitas.sh grupo Malteiro
  ```
- [ ] **1.5** Monte uma camada no Navigator com essas técnicas e salve em layers/. — [Navigator](https://github.com/mitre-attack/attack-navigator)

<a id="semana-2"></a>
## Semana 2 · Dados, versões e migração

**Entrega:** Relatório das suas regras que citam técnicas revogadas

- [ ] **2.1** Rode o diff 18.1 → 20.0 e leia as 17 técnicas que saíram.
  ```bash
  python3 scripts/attack_diff.py 18.1 20.0
  ```
- [ ] **2.2** Cruze o diff com uma pasta de regras reais (Sigma do time ou SigmaHQ).
  ```bash
  python3 scripts/attack_diff.py 18.1 20.0 --rules caminho/das/regras
  ```
- [ ] **2.3** Abra crosswalks/attack-v18.1-v20.0-substituicoes.tsv e corrija 5 regras. — [ATT&CK](https://attack.mitre.org/)
- [ ] **2.4** Instale mitreattack-python num venv e repita uma consulta da semana 1 com MitreAttackData. — [mitreattack-python](https://github.com/mitre-attack/mitreattack-python)

<a id="semana-3"></a>
## Semana 3 · Telemetria antes da regra

**Entrega:** Contrato de telemetria para 3 técnicas

- [ ] **3.1** Para T1059.001, liste evento, sensor, campos, retenção e latência usando Sensor Mappings. — [Sensor Mappings to ATT&CK](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack)
- [ ] **3.2** Registre a visibilidade dessas técnicas no DeTT&CT (modelo v18). — [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT)
- [ ] **3.3** Compare os campos que você tem com o dicionário do OSSEM e anote lacunas. — [OSSEM](https://github.com/OTRF/OSSEM)

<a id="semana-4"></a>
## Semana 4 · Detecção e robustez

**Entrega:** Uma regra Sigma convertida, versionada e avaliada

- [ ] **4.1** Gere a camada de artefatos do SigmaHQ e veja onde há material para começar.
  ```bash
  python3 scripts/coverage_layer.py sigma/rules --name Sigma -o sigma.json
  ```
- [ ] **4.2** Escolha uma regra, converta com sigma-cli para o seu SIEM e documente o pipeline de campos. — [Sigma](https://github.com/SigmaHQ/sigma), [pySigma e sigma-cli](https://github.com/SigmaHQ/pySigma)
- [ ] **4.3** Avalie a regra com Summiting the Pyramid e escreva as explicações benignas. — [Summiting the Pyramid](https://github.com/center-for-threat-informed-defense/summiting-the-pyramid), [Ambiguous Techniques](https://ctid.mitre.org/projects/ambiguous-techniques/)

<a id="semana-5"></a>
## Semana 5 · Validação purple

**Entrega:** Evidência evento → alerta → triagem

- [ ] **5.1** Rode um teste Atomic autorizado para a técnica da semana 4, com limpeza. — [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)
- [ ] **5.2** Combine as camadas Sigma × Atomic e liste 5 técnicas com regra mas sem teste.
  ```bash
  python3 scripts/coverage_layer.py --merge sigma.json atomic.json -o lacunas.json
  ```
- [ ] **5.3** Registre a campanha no VECTR ou na planilha do time. — [VECTR](https://github.com/SecurityRiskAdvisors/VECTR)
- [ ] **5.4** Para nuvem, rode uma técnica do Stratus Red Team num ambiente de teste. — [Stratus Red Team](https://github.com/DataDog/stratus-red-team)

<a id="semana-6"></a>
## Semana 6 · Defesa, resposta e forense

**Entrega:** Playbook ATT&CK → D3FEND → RE&CT para uma técnica crítica

- [ ] **6.1** Liste as contramedidas D3FEND da técnica e cheque se ela foi revogada.
  ```bash
  python3 scripts/d3fend_xwalk.py T1685 --check-revoked
  ```
- [ ] **6.2** Escreva o playbook com gatilho, dono, evidência a preservar, ação e reversão usando RE&CT e NIST 800-61r3. — [RE&CT](https://github.com/atc-project/atc-react), [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [ ] **6.3** Faça triagem de um EVTX de laboratório com Hayabusa e ligue os achados às técnicas. — [Hayabusa](https://github.com/Yamato-Security/hayabusa), [Chainsaw](https://github.com/WithSecureLabs/chainsaw)

<a id="semana-7"></a>
## Semana 7 · Vulnerabilidade como comportamento

**Entrega:** Fila de correção priorizada por técnica

- [ ] **7.1** Filtre crosswalks/cwe-capec-attack.tsv por uma CWE comum nos seus clientes.
  ```bash
  python3 scripts/capec_xwalk.py --cwe CWE-287
  ```
- [ ] **7.2** Cruze CVEs abertas com o KEV e o EPSS. — [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), [EPSS](https://www.first.org/epss/)
- [ ] **7.3** Use o Mappings Explorer (KEV → ATT&CK) para ligar CVE a técnica. — [Mappings Explorer](https://github.com/center-for-threat-informed-defense/mappings-explorer)

<a id="semana-8"></a>
## Semana 8 · CTI avançada e domínios especiais

**Entrega:** Attack Flow de um relatório real + plano INFORM

- [ ] **8.1** Modele um relatório recente no Attack Flow Builder v4.1. — [Attack Flow](https://github.com/center-for-threat-informed-defense/attack-flow)
- [ ] **8.2** Rode o TIE com as técnicas observadas e anote as previstas. — [Technique Inference Engine](https://github.com/center-for-threat-informed-defense/technique-inference-engine)
- [ ] **8.3** Escolha um domínio do seu cliente: ATLAS (IA), F3 (fraude/Pix), ICS ou AADAPT, e mapeie um cenário. — [ATLAS](https://atlas.mitre.org/), [Fight Fraud Framework](https://github.com/center-for-threat-informed-defense/fight-fraud-framework), [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/), [AADAPT](https://aadapt.mitre.org/)
- [ ] **8.4** Avalie a maturidade threat-informed do time com o INFORM e defina 3 iniciativas. — [INFORM](https://github.com/center-for-threat-informed-defense/inform)

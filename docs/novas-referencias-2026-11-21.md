# Atualização — 21/11/2026

[← Início](../README.md) · [Catálogo](catalogo.md) · [Novidades 2026](novidades-2026.md)

**O catálogo passa de 132 para 137 entradas, e 10 das 16 entradas "não verificadas" foram conferidas na fonte.** Esta revisão também junta as quatro revisões diárias de 18 a 21/11, que estavam em PRs separados.

## Cinco entradas novas

| Recurso | Para quê | Cuidado |
|---|---|---|
| [ATT&CK em Excel](https://attack.mitre.org/resources/attack-data-and-tools/) `E136` | Consultar e filtrar o ATT&CK v20.1 em planilha, sem programar | É uma exportação do STIX: para automação, use o bundle ou o `mitreattack-python` |
| [CIS Controls for Threat Mitigations](https://ctid.mitre.org/projects/cis-controls-for-threat-mitigations/) `E137` | Ver quais CIS Safeguards respondem a cada técnica | Mapeamento indica relação, não eficácia do controle no seu ambiente |
| [Prioritize Known Exploited Vulnerabilities](https://ctid.mitre.org/projects/prioritize-known-exploited-vulnerabilties/) `E138` | Priorizar CVEs do KEV pelo que o adversário faz com elas | Cobre vulnerabilidades mapeadas pelo projeto, não o KEV inteiro por definição |
| [TID for the Financial Sector](https://ctid.mitre.org/projects/tid-financial-sector/) `E139` | Justificar controles do CRI Profile por técnica adversária | O CRI Profile é uma referência do setor financeiro dos EUA; adapte ao regulador local |
| [Hardware-Enabled Defense](https://ctid.mitre.org/projects/security-stack-mappings-hardware-enabled-defense/) `E140` | Ligar recursos de segurança de hardware a técnicas do ATT&CK | Depende do hardware que você de fato tem e habilitou |

As quatro do CTID fazem parte do programa [Mappings Explorer](https://center-for-threat-informed-defense.github.io/mappings-explorer/) (`E037`): os dados são navegados e baixados por lá.

## Saíram de "não verificado"

| Entrada | Como ficou | Fonte |
|---|---|---|
| EMB3D `E005` | ativo · v2.0.2 de 01/06/2026 | seção "What's New" do site |
| SAF `E015`, Heimdall `E016`, SAF CLI `E017`, Vulcan `E018`, eMASSer `E019` | ativos · Heimdall v2.15.0, SAF CLI 1.8.0, Vulcan v2.4.2, eMASSer 3.22.0 | tags Git e data do último commit |
| Infection Monkey `E093` | ativo · v2.3.0 | tag Git; commit de 03/11/2026 |
| D3FEND Extractors `E127` | ativo | página de ferramentas do D3FEND |
| BZAR `E012`, OSSEM `E087` | baixa atividade | últimos commits em 26/06/2024 e 26/02/2023 |

Vulcan e eMASSer passaram a apontar para os próprios repositórios (`mitre/vulcan`, `mitre/emasser`) em vez do portal do SAF.

Continuam como "não verificado": CREF Navigator (o site não respondeu daqui), ECHO (a página da MITRE recusa acesso automatizado), CAVEaT, Unified Kill Chain, D3TECT e Red Team Redemption. As páginas dos quatro últimos respondem, mas são publicações ou artefatos sem sinal de manutenção que dê para ler.

## Versões

| Item | Antes | Agora |
|---|---|---|
| mitreattack-python `E028` | 6.4.0 | **6.4.1 · 18/11/2026** (PyPI) |
| ATT&CK Website `E075` | website-v4.4.1 (tag) | **v5.2.1 · 05/11/2026** pelo CHANGELOG; as versões 5.x não têm tag Git |
| Workbench `E025` | v4.19.0 | v4.19.0 estável · **v4.20.0-alpha.1** em desenvolvimento |
| Workbench REST API `E073` | v4.26.1 · alpha.1 | v4.26.1 estável · **v4.27.0-alpha.2** em desenvolvimento |
| Stratus Red Team `E090` | v2.38.0 | **v2.38.1** |
| Chainsaw `E102` | v2.17.1 | **v2.18.0** |
| Grid Watch `E133` | v2.1.1 | **v4.0.0** |
| Mappings Editor `E049` | "beta público" | **mappings_editor-v2.0.0** |

Outras 25 entradas que não tinham versão ganharam a tag Git mais recente, entre elas Adversary Emulation Library v5.0.2, TRAM v1.3.1, Insider Threat TTP KB v2.0.0, Top ATT&CK Techniques v2.0.0, ATT&CK Powered Suit v1.13.0, Sightings Ecosystem v2.0.0, OpenCTI 7.261119.0, MISP Galaxy v2.4.197, Splunk Attack Range v5.0.0, Splunk Security Content v6.11.0, OpenAEV 3.261118.0, Threatest v1.5.0 e TTPForge v1.5.0.

## Como foi conferido

- **Tags:** `git ls-remote --tags` em cada repositório, em 21/11/2026. Tag Git não é sinônimo de release estável.
- **Atividade:** data do último commit da branch padrão. Em repositórios que desenvolvem em outra branch essa data fica atrás das tags, como no Workbench.
- **Sites:** EMB3D, D3FEND, attack.mitre.org e as páginas de projeto do CTID foram lidos diretamente.
- **Sinais de manutenção:** `archived`, `license_api`, `pushed_at` e `latest_release` de 74 entradas vêm do relatório do monitor de 16/11/2026 (issue #9), gerado pela API do GitHub. `latest_release` é o que o GitHub marca como último release e pode ficar atrás das tags: no Workbench aparece `v4.6.10`, enquanto a tag estável é `v4.19.0`.
- **Não foi feito:** nenhuma ferramenta foi instalada ou executada.

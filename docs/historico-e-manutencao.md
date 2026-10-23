# Histórico, fontes e manutenção

[← Início](../README.md) · [Catálogo](catalogo.md)

## Método e limites

Revisão documental em **22/10/2026**, data local de São Paulo. Timestamps da API estão em UTC e podem aparecer como 23/10/2026.

1. Consultar portais oficiais MITRE/ATT&CK/CTID e fontes dos mantenedores.
2. Confirmar identidade e finalidade antes de classificar como oficial ou externo.
3. Inspecionar metadados GitHub de projetos selecionados, incluindo arquivamento e licença identificada pela API.
4. Separar referências históricas e registrar migrações explicitamente declaradas.
5. Selecionar P1/P2 por utilidade ao fluxo de CTI, modelagem, detecção, defesa e resposta.

A verificação foi documental: **não foram instaladas ferramentas nem testados seus resultados**. Não houve auditoria exaustiva de todos os links internos, releases ou dependências. Sites indexados podem refletir cache. Um campo `archived=false` significa apenas que o GitHub não marcou o repositório como arquivado; não certifica manutenção ativa.

`pushed_at` é sinal de atividade do repositório, não data garantida da última mudança substantiva ou do último release. `NOASSERTION` ou licença ausente na API requer leitura dos termos e arquivos relevantes; não significa domínio público ou permissão irrestrita.

## Sete repositórios históricos

| Repositório | Estado confirmado na API | Orientação |
|---|---|---|
| [attack-control-framework-mappings](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings) | Arquivado | Mapeamentos NIST migraram para Mappings Explorer, conforme descrição do repositório. |
| [security-stack-mappings](https://github.com/center-for-threat-informed-defense/security-stack-mappings) | Arquivado | Mapeamentos de stacks migraram para Mappings Explorer, conforme descrição do repositório. |
| [attack_to_cve](https://github.com/center-for-threat-informed-defense/attack_to_cve) | Arquivado | Mapeamentos CVE migraram para Mappings Explorer, conforme descrição do repositório. |
| [caldera_pathfinder](https://github.com/center-for-threat-informed-defense/caldera_pathfinder) | Arquivado | Plugin histórico de caminhos de rede; não recomendar instalação como componente atual sem revisão. |
| [attack_to_veris](https://github.com/center-for-threat-informed-defense/attack_to_veris) | Arquivado | Mapeamentos VERIS migraram para Mappings Explorer, conforme descrição do repositório. |
| [m3tid](https://github.com/center-for-threat-informed-defense/m3tid) | Arquivado | Referência histórica de maturidade; avaliar o projeto atual INFORM. Não assumir equivalência de versões ou scores. |
| [attack-workbench-collection-manager](https://github.com/center-for-threat-informed-defense/attack-workbench-collection-manager) | Arquivado | Marcado como deprecated; consultar a arquitetura atual do Workbench. |

## Atenção adicional

- **RE&CT:** não arquivado na consulta, mas `pushed_at` retornou 2022-05-31. Útil como taxonomia; revisar conteúdo e compatibilidade antes de automatizar resposta.
- **Security Datasets:** `pushed_at` retornou 2024-03-20. Datasets continuam úteis para pesquisa, mas exigem avaliação de representatividade.
- **Cloud Analytics:** `pushed_at` retornou 2023-04-25. Adaptar aos esquemas de logs e serviços atuais.
- **Engage:** o repositório consultado apontou atividade em 2024. Documentação de método não deve ser julgada só pela frequência de commits.
- **Mappings Editor:** a descrição consultada o apresenta como beta público.
- **Dados ATT&CK:** fixar versões e revisar Detection Strategies, Analytics, Data Components e mudanças de schema.
- **URLs antigas:** a pesquisa encontrou caminhos inexistentes ou redirecionados. Foram usados os destinos oficiais identificados, como `mitre/cti` e `mitre-attack/bzar`. Não usar nomes presumidos como evidência de existência.

## Fontes de descoberta e conferência

- [MITRE — Threat-Informed Defense](https://www.mitre.org/focus-areas/cybersecurity/threat-informed-defense)
- [MITRE — Capabilities & Resources](https://www.mitre.org/focus-areas/cybersecurity/capabilities-resources)
- [CTID — Our Work](https://ctid.mitre.org/projects/)
- [ATT&CK — Data & Tools](https://attack.mitre.org/resources/attack-data-and-tools/)
- [D3FEND — FAQ](https://d3fend.mitre.org/faq/)
- [SAF — portal e aplicações](https://saf.mitre.org/)
- [OASIS CTI — FAQ e governança STIX/TAXII](https://oasis-open.github.io/cti-documentation/faq.html)
- [FIRST — padrões](https://www.first.org/standards/)
- [NIST — Incident Response Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

Cada entrada do catálogo aponta para sua fonte primária. O [inventário JSON](../data/ecosystem.json) registra metadados para os repositórios consultados; campos ausentes significam **não coletado**, não um valor negativo.

## Rotina de atualização sugerida

A cada revisão, verificar redirecionamentos, arquivamento, releases, licença, novos schemas e mudanças relevantes. Comparar o catálogo de projetos CTID e recursos MITRE. Atualizar a data apenas dos itens efetivamente revisados. Preservar entradas históricas com motivo e alternativa quando houver fonte.

Não há automação agendada configurada neste repositório. A cadência sugerida é mensal para ferramentas e a cada nova versão para dados e integrações ATT&CK.

## Proveniência e licenças

O conteúdo deste repositório é uma curadoria independente com resumos e exemplos próprios. Não incorpora código, datasets completos ou logos dos projetos. Links não transferem direitos. Antes de redistribuir regras, software, imagens ou dados, consultar a licença específica e suas exceções. Marcas MITRE/ATT&CK/D3FEND e demais marcas pertencem aos respectivos titulares.

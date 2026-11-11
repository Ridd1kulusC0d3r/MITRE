<!-- ARQUIVO GERADO por python3 -m atlas build a partir de data/trilha.json. Não edite à mão. -->

# 🧗 Trilha de 8 semanas: do ATT&CK à defesa validada

[← Início](../README.md) · [Versão interativa (uma ação por vez)](../index.html#trilha) · [Catálogo](catalogo.md)

> Uma ação por vez. Cada ação termina em algo que dá para mostrar. Marque a caixa, faça a próxima. No explorador, o progresso fica salvo no seu navegador.

| Semana | Tema | Entrega |
|:-:|---|---|
| 1 | [Fundamentos do ATT&CK v20](#semana-1) | Camada Navigator com grupos que miram o Brasil e a LATAM |

<a id="semana-1"></a>
## Semana 1 · Fundamentos do ATT&CK v20

**Entrega:** Camada Navigator com grupos que miram o Brasil e a LATAM

- [ ] **1.1** Leia a página de uma técnica que você já detecta (ex.: T1059.001) e anote procedimento, Detection Strategy e mitigação. — [ATT&CK](https://attack.mitre.org/)
- [ ] **1.2** Rode scripts/fetch_all.sh e confira o manifesto com SHA-256.
  ```bash
  ./scripts/fetch_all.sh
  ```
- [ ] **1.3** Gere a lista de técnicas por tática e conte quantas estão em Defense Impairment.
  ```bash
  python3 scripts/attack_dump.py --file data/cache/enterprise-attack-20.0.json > tecnicas.md
  ```

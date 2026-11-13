# Mini-sistema de estoque (UC3 — Realizar testes e manutenção)

Sistema simples de controle de estoque em Python, com menu no terminal e dados gravados em `dados/produtos.json`.

> Este sistema **tem defeitos de propósito**. Seu trabalho ao longo da UC3 é encontrá-los, registrá-los, corrigi-los e provar a correção com testes.

## Como rodar

```bash
python main.py          # abre o menu
python -m pytest -v     # roda os testes
```

## Estrutura

```
estoque/
  validacoes.py     # validação de nome, preço e quantidade
  produtos.py       # regras de negócio (cadastro, busca, estoque, desconto)
  persistencia.py   # salvar/carregar JSON, backup e restore
main.py             # menu no terminal
tests/              # seus testes ficam aqui
```

## Regras do sistema (use como especificação)

- Nome: obrigatório (não pode ser vazio).
- Preço: número maior que zero.
- Quantidade: inteiro maior ou igual a zero (estoque zerado é permitido).
- Cada produto tem um **id único**, mesmo depois de remoções.
- Busca por nome: parcial e sem diferenciar maiúsculas de minúsculas.
- Retirada de estoque: não pode deixar a quantidade negativa.
- Valor total do estoque: soma de preço × quantidade de cada produto.
- Desconto: percentual de 0 a 100 (inclusive).
- Estoque baixo: produtos com quantidade menor ou igual ao limite (padrão 5).
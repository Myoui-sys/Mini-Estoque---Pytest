# Testes Automatizados 

## Tecnologias: Python e Pytest

## BUG 001 — Geração de ID duplicado após remoção

- **Função:** `proximo_id()`
- **Status:** Defeito identificado.

**Descrição:**  
A função gera o próximo ID considerando a quantidade de produtos cadastrados (`len(produtos) + 1`), em vez de considerar o maior ID já utilizado. Com isso, após a remoção de um produto, existe a possibilidade de reutilizar um ID.

**Cenário de teste:**  
Foi criada uma lista de produtos contendo os IDs 1 e 3, simulando a remoção do produto com ID 2. Ao solicitar o próximo ID, o resultado esperado era 4, garantindo que nenhum identificador anterior fosse reutilizado.

**Evidência do Pytest:**
```text
FAILED tests/test_produtos.py::test_proximo_id_apos_remocao
assert 3 == 4
```

**Resultado:**  
<escape>O teste falhou, confirmando que a função retornou o ID 3, embora o esperado fosse 4.</escape>

**Causa provável:**  
A lógica atual utiliza a quantidade de elementos da lista para calcular o próximo identificador, não considerando os IDs existentes.

## BUG 002 — Buscar nome sem diferenciar maiúsculas e minúsculas

- **Função:** `buscar_por_nome()`
- **Status:** Defeito identificado.

**Descrição:**  
A função realiza a busca considerando a diferença entre letras maiúsculas e minúsculas. Isso faz com que um produto não seja encontrado quando o termo pesquisado possui uma capitalização diferente do nome cadastrado.

**Cenário de teste:**  
Foi cadastrado um produto com o nome "Caneta". Em seguida, foi realizada uma busca pelo termo "caneta", utilizando apenas letras minúsculas.

**Evidência do Pytest:**
```text
FAILED tests/test_produtos.py::test_buscar_por_nome[caneta] - IndexError: list index out of range
FAILED tests/test_produtos.py::test_buscar_por_nome[CANETA] - IndexError: list index out of range
```

**Resultado:**  
<escape>O teste falhou porque a função não encontrou o produto cadastrado, embora o nome correspondesse ao termo pesquisado.</escape>

**Causa provável:**  
A comparação é realizada diretamente, sem converter o nome do produto e o termo pesquisado para o mesmo padrão de letras.
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

## BUG 003 — Retirar estoque maior que disponível

- **Função:** `retirar_estoque()`
- **Status:** Defeito identificado.

**Descrição:**  
A função permite retirar uma quantidade maior do que a disponível no estoque, fazendo com que a quantidade do produto fique negativa.

**Cenário de teste:**  
Foi criado um produto com 5 unidades disponíveis. Em seguida, foi solicitada a retirada de 10 unidades, esperando que o sistema impedisse a operação e gerasse um ValueError.

**Evidência do Pytest:**
```text
FAILED tests/test_produtos.py::test_retirar_estoque_maior_que_disponivel
Failed: DID NOT RAISE ValueError
```

**Resultado:**  
<escape>O teste falhou porque a função permitiu a retirada de uma quantidade superior ao estoque disponível, sem gerar a exceção esperada.</escape>

**Causa provável:**  
A função não possui uma verificação para impedir que a quantidade solicitada seja maior que a quantidade disponível no estoque.

## BUG 003 — Cálculo do valor total do estoque (Soma do preço * quantidade de cada produto)

- **Função:** `valor_total_estoque()`
- **Status:** Defeito identificado.

**Descrição:**  
A função soma apenas o preço dos produtos, sem multiplicar pelo total de unidades disponíveis em estoque.

**Cenário de teste:**  
Foram cadastrados dois produtos: uma Caneta, com preço de R$ 50,00 e quantidade 2, e uma Tinta Amarela, com preço de R$ 5,00 e quantidade 10. O valor esperado era R$ 150,00.

**Evidência do Pytest:**
```text
FAILED tests/test_produtos.py::test_valor_total_estoque - assert 55.0 == 150.0
```

**Resultado:**  
<escape>O teste falhou porque a função retornou R$ 55,00, somando apenas os preços dos produtos, em vez de calcular o valor total considerando suas quantidades.</escape>

**Causa provável:**  
A função não multiplica o preço pela quantidade de cada produto antes de somar os valores.
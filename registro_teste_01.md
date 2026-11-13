# Aula 01 - UC3

## Registro BUG - 01

- Resultado esperado: Cada produto tem um **id único**, mesmo depois de remoções.
- Resultado obtido: Cadastrar um novo produto após a removação de um produto, contato que o produto não seja o último da lista, este novo produto é cadastrado com o mesmo ID do último da lista. 
- Status: Falhou

## Registro BUG - 02

- Resultado esperado: Busca por nome: parcial e sem diferenciar maiúsculas de minúsculas.
- Resultado obtido: Diferencia maiúscula de minúscula.
- Status: Falhou

## Registro BUG - 03

- Resultado esperado: Retirada de estoque: não pode deixar a quantidade negativa.
- Resutado obtido: Após colocar uma quantidade maior do que o produto tinha no estoque, a quantidade ficou negativa.
- Status: Falhou

## Registro BUG - 04

- Resultado esperado: Valor total do estoque: soma de preço × quantidade de cada produto.
- Resutado obtido: Não está somando o preço dos produtos x quantidade. Caneta no preço de R$50.00 e 2 Qtd, Tinta Amarela R$5.00 e 10 Qtd, deveria dar R$150.00, mas deu R$55, apenas somando os preços dos dois produtos.
- Status: Falhou

## Registro BUG - 05

- Resultado esperado: Estoque baixo: produtos com quantidade menor ou igual ao limite (padrão 5).
- Resutado obtido: Produtos com a quantidade de estoque igual a 5 não aparecem na opção de Estoque Baixo.
- Status: Falhou
import pytest

from estoque.validacoes import (validar_quantidade, validar_preco, validar_nome)

# Para validar o nome: 
# nome comum
# nome com espaços nas pontas
# entradas inválidas: texto vazio, só espaços, None e número 

# Passou
@pytest.mark.parametrize("nome", [
    "",
    "        ",
    None,
    30
])
def test_validar_nome(nome):
    with pytest.raises(ValueError):
        validar_nome(nome)

# Para validar preço:
# preços que a regra não aceita (use o valor do limite e um valor abaixo dele)
# o menor valor que a regra aceita, logo acima do limite entradas não numéricas: "abc", "" e None

#Passou
@pytest.mark.parametrize("preco", [
    "ABC",
    "",
    None,
    -1
])
def test_validar_preco(preco):
    with pytest.raises(ValueError):
        validar_preco(preco)


# Para validar quantidade: 

# um valor logo abaixo do limite
# tipos inválidos: decimal, texto, booleano e None (parametrize)
# maior ou igual a zero inteiro

@pytest.mark.parametrize("quantidade", [
    -1,
    10.2,
    "ABC",
    True,
    None
])
def test_validar_quantidade(quantidade):
    with pytest.raises(ValueError):
        validar_quantidade(quantidade)

# Passou
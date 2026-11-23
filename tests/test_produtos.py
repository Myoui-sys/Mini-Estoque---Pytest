import pytest

from estoque.produtos import (proximo_id, buscar_por_nome, cadastrar_produto, calcular_desconto, estoque_baixo, remover_produto, repor_estoque, retirar_estoque, valor_total_estoque, _obter)

# FIXTURES

@pytest.fixture
def produtos():
    return [
        # Valor-limite: uma unidade abaixo do limite (4)
        {"id": 1, "nome": "Caneta", "preco": 2.5, "quantidade": 4},

        # Valor-limite: exatamente no limite (5)
        {"id": 2, "nome": "Caderno", "preco": 15.0, "quantidade": 5},

        # Valor-limite: uma unidade acima do limite (6)
        {"id": 3, "nome": "Lápis", "preco": 1.0, "quantidade": 6},

        # Valor-limite mínimo: estoque zerado
        {"id": 4, "nome": "Borracha", "preco": 2.0, "quantidade": 0},

        # Partição de equivalência: estoque distante do limite
        {"id": 5, "nome": "Régua", "preco": 5.0, "quantidade": 20}
    ]

@pytest.fixture
def produtos_vazios():
    # Prepara uma lista vazia para os testes de cadastro.
    return []

@pytest.fixture
def produtos_com_id_removido():
    # Simula uma lista em que um produto foi removido,
    # mantendo os IDs 1 e 3.
    return [
        {"id": 1, "nome": "Caneta"},
        {"id": 3, "nome": "Borracha"}
    ]

# Função de teste para próximo ID (não pode se repetir) após um produto ser removido
def test_proximo_id_apos_remocao(produtos_com_id_removido):

    resultado = proximo_id(produtos_com_id_removido)

    assert resultado == 4

# Função de teste para cadastrar produto
@pytest.mark.parametrize("nome, preco, quantidade", [
    ("Lápis", 1.0, 2),
    ("Caderno", 15.0, 5),
    ("Caneta", 2.5, 10)
])
def test_cadastrar_produto(produtos_vazios, nome, preco, quantidade):

    resultado = cadastrar_produto(produtos_vazios, nome, preco, quantidade)

    assert resultado["nome"] == nome
    assert resultado["preco"] == preco
    assert resultado["quantidade"] == quantidade
    assert resultado["id"] == 1
    assert len(produtos_vazios) == 1

# Função de teste para diferenciar maiúscula por minúscula e parcial
@pytest.mark.parametrize("nome", [
    "caneta",
    "CANETA",
    "Caneta",
    "neta"
])
def test_buscar_por_nome(produtos, nome):

    resultado = buscar_por_nome(produtos, nome)

    assert resultado[0]["nome"] == "Caneta"

# Função de buscar produto por ID
def test_obter_produto(produtos):

    resultado = _obter(produtos, 2)

    assert resultado["nome"] == "Caderno"

# Função de teste para remover produto
def test_remover_produto(produtos):

    resultado = remover_produto(produtos, 1)

    assert resultado["id"] == 1
    assert len(produtos) == 4

# Função de teste para repor estoque
def test_repor_estoque(produtos):
    produto = repor_estoque(produtos, 1, 5)

    assert produto["quantidade"] == 9

# Função de teste para retirar estoque de um produto, sem deixar negativo
def test_retirar_estoque_maior_que_disponivel(produtos):

    with pytest.raises(ValueError):
        retirar_estoque(produtos, 1, 10)

# Função de teste para calcular o valor total do estoque
def test_valor_total_estoque(produtos):

    resultado = valor_total_estoque(produtos)

    assert resultado == 191.0

# Função de teste para calcular o desconto
@pytest.mark.parametrize("percentual, esperado", [
    (0, 100),
    (10, 90),
    (50, 50),
    (100, 0)
])
def test_calcular_desconto(percentual, esperado):

    resultado = calcular_desconto(100, percentual)

    assert resultado == esperado

# Função de testar o limite de produtos que aparecem com o estoque baixo
def test_estoque_baixo(produtos):

    resultado = estoque_baixo(produtos)

    assert len(resultado) == 3
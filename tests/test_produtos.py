import pytest

from estoque.produtos import (proximo_id, buscar_por_nome, cadastrar_produto, calcular_desconto, estoque_baixo, remover_produto, repor_estoque, retirar_estoque, validar_nome, validar_preco, validar_quantidade, valor_total_estoque, _obter)

# Função de teste para próximo ID (não pode se repetir) após um produto ser removido
def test_proximo_id_apos_remocao():
    produtos = [
        {"id": 1, "nome": "Caneta"},
        {"id": 3, "nome": "Borracha"}
    ]

    resultado = proximo_id(produtos)

    assert resultado == 4

# Função de teste para cadastrar produto
@pytest.mark.parametrize("nome, preco, quantidade", [
    ("Lápis", 1.0, 2),
    ("Caderno", 15.0, 5),
    ("Caneta", 2.5, 10)
])
def test_cadastrar_produto(nome, preco, quantidade):
    produtos = []

    resultado = cadastrar_produto(produtos, nome, preco, quantidade)

    assert resultado["nome"] == nome
    assert resultado["preco"] == preco
    assert resultado["quantidade"] == quantidade
    assert resultado["id"] == 1
    assert len(produtos) == 1


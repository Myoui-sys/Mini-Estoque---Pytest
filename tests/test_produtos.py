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
def test_cadastrar_produto():
    produtos = []

    resultado = cadastrar_produto(produtos, "Lápis", 1.0, 2)

    assert resultado["nome"] == "Lápis"
    assert resultado["preco"] == 1.0
    assert resultado["quantidade"] == 2
    assert resultado["id"] == 1
    assert len(produtos) == 1
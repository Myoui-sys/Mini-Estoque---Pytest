import pytest

from estoque.produtos import (proximo_id, buscar_por_nome, cadastrar_produto, calcular_desconto, estoque_baixo, remover_produto, repor_estoque, retirar_estoque, validar_nome, validar_preco, validar_quantidade, valor_total_estoque, _obter)

# Função teste de não repetir ID após a remoção de um produto
# lista vazia
# lista com produtos
# depois de remover um produto do meio da lista
def test_proximo_id_apos_remocao():
    produtos = [
        {"id": 1, "nome": "Caneta"},
        {"id": 3, "nome": "Borracha"}
    ]

    resultado = proximo_id(produtos)

    assert resultado == 4


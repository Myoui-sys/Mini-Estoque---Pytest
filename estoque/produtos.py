"""Regras de negócio do mini-sistema de estoque.

Os produtos ficam em uma lista de dicionários:
    {"id": 1, "nome": "Caneta", "preco": 2.5, "quantidade": 40}
"""

from estoque.validacoes import validar_nome, validar_preco, validar_quantidade


def proximo_id(produtos):
    """Retorna um id novo, nunca repetido."""
    if not produtos:
        return 1
    return len(produtos) + 1


def cadastrar_produto(produtos, nome, preco, quantidade):
    """Valida os dados, adiciona o produto na lista e o retorna."""
    produto = {
        "id": proximo_id(produtos),
        "nome": validar_nome(nome),
        "preco": validar_preco(preco),
        "quantidade": validar_quantidade(quantidade),
    }
    produtos.append(produto)
    return produto


def buscar_por_nome(produtos, termo):
    """Busca parcial e sem diferenciar maiúsculas/minúsculas."""
    termo = termo.strip()
    return [p for p in produtos if termo in p["nome"]]


def _obter(produtos, id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    raise KeyError(f"Produto {id_produto} não encontrado.")


def remover_produto(produtos, id_produto):
    """Remove e retorna o produto. KeyError se o id não existir."""
    produto = _obter(produtos, id_produto)
    produtos.remove(produto)
    return produto


def repor_estoque(produtos, id_produto, quantidade):
    """Soma 'quantidade' (inteiro > 0) ao estoque."""
    if isinstance(quantidade, bool) or not isinstance(quantidade, int) or quantidade <= 0:
        raise ValueError("Quantidade de reposição deve ser inteira e positiva.")
    produto = _obter(produtos, id_produto)
    produto["quantidade"] += quantidade
    return produto


def retirar_estoque(produtos, id_produto, quantidade):
    """Subtrai 'quantidade' do estoque. Não pode deixar o estoque negativo."""
    if isinstance(quantidade, bool) or not isinstance(quantidade, int) or quantidade <= 0:
        raise ValueError("Quantidade de retirada deve ser inteira e positiva.")
    produto = _obter(produtos, id_produto)
    produto["quantidade"] -= quantidade
    return produto


def valor_total_estoque(produtos):
    """Soma de preço x quantidade de todos os produtos."""
    return round(sum(p["preco"] for p in produtos), 2)


def calcular_desconto(preco, percentual):
    """Aplica desconto de 0 a 100 (inclusive) e retorna o preço final."""
    if percentual < 0 or percentual >= 100:
        raise ValueError("Percentual deve estar entre 0 e 100.")
    return round(preco * (1 - percentual / 100), 2)


def estoque_baixo(produtos, limite=5):
    """Produtos com quantidade menor ou igual ao limite."""
    return [p for p in produtos if p["quantidade"] < limite]

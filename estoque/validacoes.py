"""Validações de entrada do mini-sistema de estoque."""


def validar_nome(nome):
    """Retorna o nome sem espaços nas pontas. Levanta ValueError se vazio."""
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    return nome.strip()


def validar_preco(preco):
    """Converte para float (2 casas). O preço deve ser maior que zero."""
    try:
        valor = float(preco)
    except (TypeError, ValueError):
        raise ValueError("Preço deve ser numérico.")
    if valor <= 0:
        raise ValueError("Preço deve ser maior que zero.")
    return round(valor, 2)


def validar_quantidade(quantidade):
    """Quantidade deve ser inteira e >= 0 (estoque zerado é permitido)."""
    if isinstance(quantidade, bool) or not isinstance(quantidade, int):
        raise ValueError("Quantidade deve ser um número inteiro.")
    if quantidade <= 0:
        raise ValueError("Quantidade não pode ser negativa.")
    return quantidade

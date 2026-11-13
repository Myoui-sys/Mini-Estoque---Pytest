"""Primeiro teste com pytest (Aula 2). Rode com:  python -m pytest -v"""

from estoque.validacoes import validar_nome


def test_nome_remove_espacos():
    assert validar_nome("  Caneta  ") == "Caneta"

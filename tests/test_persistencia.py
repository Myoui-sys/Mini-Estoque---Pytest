import json
import os
import pytest

from estoque.persistencia import (salvar, carregar, fazer_backup, restaurar_backup)

# FIXTURES

@pytest.fixture
def caminho_json(tmp_path):
    # Cria um caminho para um arquivo JSON temporário.
    return tmp_path / "produtos.json"

@pytest.fixture
def produtos():
    # Prepara produtos para testar a gravação e leitura.
    return [
        {"id": 1, "nome": "Caneta", "preco": 2.5, "quantidade": 5},
        {"id": 2, "nome": "Caderno", "preco": 15.0, "quantidade": 0},
        {"id": 3, "nome": "Lápis", "preco": 1.0, "quantidade": 10}
    ]

@pytest.fixture
def arquivo_json(caminho_json, produtos):
    # Salva os produtos no arquivo temporário para reutilizar nos testes.
    salvar(produtos, str(caminho_json))
    return caminho_json

@pytest.fixture
def backup(arquivo_json, tmp_path):
    # Cria um backup do arquivo JSON para os testes de restauração.
    pasta_backup = tmp_path / "backups"
    return fazer_backup(str(arquivo_json), str(pasta_backup))

# TESTES DE SALVAMENTO

def test_salvar_produtos(caminho_json, produtos):

    salvar(produtos, str(caminho_json))

    assert caminho_json.exists()

def test_salvar_cria_pasta(caminho_json, produtos):

    salvar(produtos, str(caminho_json))

    assert caminho_json.parent.exists()

# TESTES DE CARREGAMENTO

def test_carregar_produtos(arquivo_json, produtos):

    resultado = carregar(str(arquivo_json))

    assert resultado == produtos

def test_carregar_arquivo_inexistente(tmp_path):

    caminho = tmp_path / "inexistente.json"

    resultado = carregar(str(caminho))

    assert resultado == []

# TESTES DE BACKUP

def test_fazer_backup(arquivo_json, tmp_path):

    resultado = fazer_backup(
        str(arquivo_json),
        str(tmp_path / "backups")
    )

    assert os.path.exists(resultado)
    assert resultado.endswith(".bak")

def test_fazer_backup_arquivo_inexistente(tmp_path):

    caminho = tmp_path / "inexistente.json"

    with pytest.raises(FileNotFoundError):
        fazer_backup(str(caminho))

# TESTES DE RESTAURAÇÃO

def test_restaurar_backup(backup, tmp_path, produtos):

    destino = tmp_path / "restaurado.json"

    resultado = restaurar_backup(str(backup), str(destino))

    assert resultado == str(destino)
    assert destino.exists()

    with open(destino, encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    assert dados == produtos

def test_restaurar_backup_inexistente(tmp_path):

    backup_inexistente = tmp_path / "backup_inexistente.bak"
    destino = tmp_path / "restaurado.json"

    with pytest.raises(FileNotFoundError):
        restaurar_backup(str(backup_inexistente), str(destino))
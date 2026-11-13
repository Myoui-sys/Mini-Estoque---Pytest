"""Gravação e leitura dos produtos em arquivo JSON, mais backup/restore."""

import json
import os
import shutil
from datetime import datetime


def salvar(produtos, caminho):
    """Grava a lista de produtos em JSON (cria a pasta se necessário)."""
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=2)


def carregar(caminho):
    """Lê a lista de produtos. Se o arquivo não existir, retorna lista vazia."""
    if not os.path.exists(caminho):
        return []
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)


def fazer_backup(caminho, pasta_backup="backups"):
    """Copia o arquivo de dados para a pasta de backup com data e hora."""
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo {caminho} não existe.")
    os.makedirs(pasta_backup, exist_ok=True)
    carimbo = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome = f"{os.path.basename(caminho)}.{carimbo}.bak"
    destino = os.path.join(pasta_backup, nome)
    shutil.copy2(caminho, destino)
    return destino


def restaurar_backup(caminho_backup, caminho_destino):
    """Restaura um backup sobre o arquivo de dados."""
    if not os.path.exists(caminho_backup):
        raise FileNotFoundError(f"Backup {caminho_backup} não existe.")
    shutil.copy2(caminho_backup, caminho_destino)
    return caminho_destino

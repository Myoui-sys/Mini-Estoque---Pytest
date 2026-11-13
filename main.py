"""Interface de linha de comando do mini-sistema de estoque.

Execute com:  python main.py
"""

from estoque.persistencia import carregar, fazer_backup, salvar
from estoque.produtos import (
    buscar_por_nome,
    cadastrar_produto,
    estoque_baixo,
    remover_produto,
    repor_estoque,
    retirar_estoque,
    valor_total_estoque,
)

ARQUIVO = "dados/produtos.json"

MENU = """
===== CONTROLE DE ESTOQUE =====
1 - Cadastrar produto
2 - Listar produtos
3 - Buscar por nome
4 - Repor estoque
5 - Retirar estoque
6 - Remover produto
7 - Estoque baixo
8 - Valor total do estoque
9 - Fazer backup
0 - Sair
"""


def mostrar(produtos):
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    print(f"{'ID':<4}{'Nome':<25}{'Preço':>10}{'Qtd':>6}")
    for p in produtos:
        print(f"{p['id']:<4}{p['nome']:<25}{p['preco']:>10.2f}{p['quantidade']:>6}")


def main():
    produtos = carregar(ARQUIVO)
    while True:
        print(MENU)
        opcao = input("Opção: ").strip()
        try:
            if opcao == "1":
                nome = input("Nome: ")
                preco = input("Preço: ").replace(",", ".")
                quantidade = int(input("Quantidade: "))
                cadastrar_produto(produtos, nome, preco, quantidade)
                salvar(produtos, ARQUIVO)
                print("Produto cadastrado.")
            elif opcao == "2":
                mostrar(produtos)
            elif opcao == "3":
                mostrar(buscar_por_nome(produtos, input("Termo: ")))
            elif opcao == "4":
                repor_estoque(produtos, int(input("ID: ")), int(input("Quantidade: ")))
                salvar(produtos, ARQUIVO)
                print("Estoque atualizado.")
            elif opcao == "5":
                retirar_estoque(produtos, int(input("ID: ")), int(input("Quantidade: ")))
                salvar(produtos, ARQUIVO)
                print("Estoque atualizado.")
            elif opcao == "6":
                remover_produto(produtos, int(input("ID: ")))
                salvar(produtos, ARQUIVO)
                print("Produto removido.")
            elif opcao == "7":
                mostrar(estoque_baixo(produtos))
            elif opcao == "8":
                print(f"Valor total: R$ {valor_total_estoque(produtos):.2f}")
            elif opcao == "9":
                print("Backup criado em:", fazer_backup(ARQUIVO))
            elif opcao == "0":
                print("Até logo!")
                break
            else:
                print("Opção inválida.")
        except (ValueError, KeyError, FileNotFoundError) as erro:
            print("Erro:", erro)


if __name__ == "__main__":
    main()

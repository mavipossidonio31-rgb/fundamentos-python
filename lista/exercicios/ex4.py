def remover_produto(produtos, produto):
    produtos.remove(produto)


produtos = ["Arroz", "Feijão", "Leite", "Pão"]

print("Lista no começo:", produtos)

produto = input("Digite o produto que deseja remover: ")

remover_produto(produtos, produto)

print("Lista no fim:", produtos)
def adicionar_produtos(compras, produtos):
    compras.extend(produtos)


def cancelar_compra(compras, produto):
    compras.remove(produto)


compras = ["Arroz", "Feijão", "Leite"]

produtos = ["Pão", "Café"]

adicionar_produtos(compras, produtos)

print("Compras:", compras)

produto = input("Digite o produto que deseja cancelar: ")

cancelar_compra(compras, produto)

print("Compras depois:", compras)
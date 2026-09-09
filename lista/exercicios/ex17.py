def vender_produto(estoque, produto):

    if produto in estoque:

        estoque.remove(produto)

        print("Produto vendido!")

    else:

        print("Produto não está disponível.")

    return estoque


estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

produto = input("Digite o produto que deseja comprar: ")

estoque = vender_produto(estoque, produto)

print("Estoque:", estoque)
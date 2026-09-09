def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    return posicao


produtos = ["Mouse", "Teclado", "Monitor", "Webcam"]

produto = input("Digite o produto: ")


print("O produto está na posição:", resultado)

resultado = encontrar_produto(produtos, produto)

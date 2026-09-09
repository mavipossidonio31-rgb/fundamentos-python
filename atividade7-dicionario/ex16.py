def lista_compras():
    compra = {
        "cliente": "Maria",
        "produtos": []
    }

    print("Digite 5 produtos para a compra:")
    for i in range(5):
        produto = input(f"Produto {i + 1}: ")
        compra["produtos"].append(produto)

    print("\n--- RESUMO DA COMPRA ---")
    print("Cliente:", compra["cliente"])
    print("Produtos comprados:", compra["produtos"])


lista_compras()
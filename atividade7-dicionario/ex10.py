def controle_estoque():
    produto = {
        "nome": "Mouse",
        "preco": 80,
        "estoque": 10
    }

    print(f"Estoque atual de {produto['nome']}: {produto['estoque']} unidades.")
    vendido = int(input("Digite a quantidade vendida: "))

    # Verificando se tem estoque suficiente para não ficar negativo
    if vendido <= produto["estoque"]:
        produto["estoque"] -= vendido
        print(f"Venda realizada! Novo estoque: {produto['estoque']}")
    else:
        print("Erro: A quantidade vendida é maior do que o estoque disponível!")


controle_estoque()
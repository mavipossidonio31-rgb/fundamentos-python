def reajuste_preco():
    produto = {
        "nome": "Teclado",
        "preco": 100.00
    }

    print(f"Preço atual: R$ {produto['preco']:.2f}")
    aumento = float(input("Digite o percentual de aumento (ex: 10 para 10%): "))

    novo_preco = produto["preco"] + (produto["preco"] * aumento / 100)
    produto["preco"] = novo_preco

    print(f"Novo preço: R$ {produto['preco']:.2f}")


reajuste_preco()
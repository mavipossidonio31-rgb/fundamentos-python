def cadastro_dinamico():
    dados = {}

    quantidade = int(input("Quantas informações deseja cadastrar? "))

    for i in range(quantidade):
        chave = input(f"Digite o nome da {i + 1}ª chave: ")
        valor = input(f"Digite o valor para '{chave}': ")
        dados[chave] = valor

    print("\n--- dicionario final ---")
    print(dados)


cadastro_dinamico()
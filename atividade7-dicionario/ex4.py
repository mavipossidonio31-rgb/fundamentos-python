def verificar_chave():
    usuario = {
        "nome": "Pedro",
        "idade": 30,
        "cidade": "Rio de Janeiro"
    }

    chave = input("Digite o nome da chave que deseja buscar (ex: nome, idade, cpf): ")

    if chave in usuario:
        print(f"A chave '{chave}' existe no dicionário!")
    else:
        print(f"A chave '{chave}' NÃO existe no dicionário.")


verificar_chave()
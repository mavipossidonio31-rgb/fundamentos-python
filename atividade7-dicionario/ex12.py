def remover_telefone():
    funcionario = {
        "nome": "Fernanda",
        "idade": 28,
        "cargo": "Gerente",
        "salario": 4500.00,
        "telefone": "91111-2222"
    }

    print("1. Dicionário antes da remoção:")
    print(funcionario)


    telefone_removido = funcionario.pop("telefone")

    print("\n2. O telefone removido foi:", telefone_removido)
    print("\n3. Dicionário depois da remoção:")
    print(funcionario)


remover_telefone()
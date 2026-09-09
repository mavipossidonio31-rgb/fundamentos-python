def adicionar_informacoes():
    usuario = {
        "nome": "Mariana",
        "idade": 25
    }

    usuario["email"] = input("Digite o email: ")
    usuario["endereço"] = input("Digite o endereço: ")
    usuario["telefone"] = input("Digite o telefone: ")

    print("\n--- informacoes cadastradas ---")
    print("Nome:", usuario["nome"])
    print("Idade:", usuario["idade"])
    print("Email:", usuario["email"])
    print("Endereço:", usuario["endereço"])
    print("Telefone:", usuario["telefone"])


adicionar_informacoes()
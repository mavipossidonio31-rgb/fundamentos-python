def limpar_cadastro():
    funcionario = {
        "nome": "Roberto",
        "idade": 40,
        "cargo": "Analista",
        "salario": 3500.00,
        "telefone": "93333-4444"
    }

    print("Dicionário original:", funcionario)

    del funcionario["telefone"]

    print("Dicionário atualizado após remover o telefone:", funcionario)


limpar_cadastro()
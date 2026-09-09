def consultar_cliente():
    cliente = {
        "nome": "Lucas",
        "idade": 22,
        "cidade": "Curitiba"
    }

    informacao = input("Qual informação deseja consultar (nome, idade, cidade, profissao...)? ")

    resultado = cliente.get(informacao, "Informação não encontrada.")
    print("Resultado:", resultado)


consultar_cliente()
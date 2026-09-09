def separar_nome(nome_completo):
    nomes = nome_completo.split()

    for nome in nomes:
        print(nome)


nome_completo = input("digite seu nome completo: ")

separar_nome(nome_completo)
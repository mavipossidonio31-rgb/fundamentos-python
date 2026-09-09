def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)


nomes = ["Maria", "João"]

nome = input("Digite um nome: ")

adicionar_nome(nomes, nome)
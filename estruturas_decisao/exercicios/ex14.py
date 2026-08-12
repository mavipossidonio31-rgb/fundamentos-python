def sistema_votacao():
    idade = int(input("Digite a sua idade: "))

    if idade < 16:
        print("não pode votar")
    elif idade < 18 or idade >= 70:
        print("voto opcional")
    else:
        print("voto obrigatório")


sistema_votacao()
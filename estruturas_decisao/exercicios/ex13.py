def preco_ingresso():
    idade = int(input("Digite a sua idade: "))

    if idade <= 5:
        print("ingresso gratuito")
    elif idade <= 12:
        print("preço do ingresso: R$ 10,00")
    elif idade <= 59:
        print("preço do ingresso: R$ 20,00")
    else:
        print("preço do ingresso: R$ 10,00")


preco_ingresso()
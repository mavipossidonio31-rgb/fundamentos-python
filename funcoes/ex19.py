
def consumo_energia():
    consumo = float(input("Digite o consumo em kWh: "))
    preco = float(input("Digite o preço do kWh: "))

    conta = consumo * preco

    print("O valor da conta é: R$", conta)


consumo_energia()
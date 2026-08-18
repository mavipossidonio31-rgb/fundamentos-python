def frete():
    compra = float(input("digite o valor da compra: "))

    if compra <= 100:
        valor_frete = 20
    elif compra <= 300:
        valor_frete = 10
    else:
        valor_frete = 0

    total = compra + valor_frete

    print("Valor da compra:", compra)
    print("Valor do frete:", valor_frete)
    print("Valor total:", total)


frete()
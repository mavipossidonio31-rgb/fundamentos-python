def classificar_temperatura():
    celsius =float(input("digite a temperatura em graus Celsius: "))

    if celsius > 15:
        print("frio")
    elif celsius <= 25:
        print("agradavel")
    else:
        print("quente")
classificar_temperatura()

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)


numero = int(input("digite um número: "))

tabuada(numero)
def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado

numero = int(input("digite um número: "))

resultado = fatorial(numero)

print("fatorial:", resultado)
def inverter_lista(lista):
    lista_invertida = list(reversed(lista))
    return lista_invertida


numeros = [1, 2, 3, 4, 5]

print("Lista no começo:", numeros)

resultado = inverter_lista(numeros)

print("Lista invertida:", resultado)
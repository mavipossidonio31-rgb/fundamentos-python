def ordenar_numeros(numeros):
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados


numeros = [8, 2, 5, 1, 9, 3]

print("Lista no começo:", numeros)

resultado = ordenar_numeros(numeros)

print("Lista ordenada:", resultado)
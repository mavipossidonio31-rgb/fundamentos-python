def ordenar_nomes(nomes):
    nomes_ordenados = sorted(nomes)
    return nomes_ordenados


nomes = ["Carlos", "Maria", "Ana", "João", "Pedro"]

print("Lista no começo:", nomes)

resultado = ordenar_nomes(nomes)

print("Lista em ordem alfabética:", resultado)
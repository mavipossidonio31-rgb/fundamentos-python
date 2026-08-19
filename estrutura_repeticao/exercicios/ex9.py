
def contar_pares(inicio, fim):
    quantidade = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            quantidade = quantidade + 1

    return quantidade


inicio = int(input("digite o início: "))
fim = int(input("digite o fim: "))

resultado = contar_pares(inicio, fim)

print("Quantidade de números pares:", resultado)
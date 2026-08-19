def somar_pares(inicio, fim):
    soma = 06
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma += i
    return soma

# Entrada de dados, chamada da função e exibição do resultado
inicio_range = int(input("Digite o número inicial: "))
fim_range = int(input("Digite o número final: "))

resultado = somar_pares(inicio_range, fim_range)
print(f"A soma dos números pares entre {inicio_range} e {fim_range} é: {resultado}")
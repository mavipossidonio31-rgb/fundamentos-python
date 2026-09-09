def analisar_temperaturas(temperaturas):

    quantidade = len(temperaturas)

    soma = sum(temperaturas)

    media = soma / quantidade

    temperaturas = sorted(temperaturas)

    return quantidade, soma, media, temperaturas


temperaturas = [25, 30, 22, 28, 20]

resultado = analisar_temperaturas(temperaturas)

print("Quantidade:", resultado[0])

print("Soma:", resultado[1])

print("Média:", resultado[2])

print("Temperaturas ordenadas:", resultado[3])
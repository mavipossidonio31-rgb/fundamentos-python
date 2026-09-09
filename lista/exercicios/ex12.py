def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)

    media = soma / quantidade

    return media


notas = [7, 8, 9, 6]

resultado = calcular_media(notas)

print("A média é:", resultado)
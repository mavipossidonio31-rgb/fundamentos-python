def adicionar_nota(notas, nota):
    notas.append(nota)


def remover_nota(notas, nota):
    notas.remove(nota)


def media_notas(notas):
    media = sum(notas) / len(notas)
    return media


notas = [7, 8, 6]

nota = float(input("Digite uma nota: "))

adicionar_nota(notas, nota)

print("Notas:", notas)

nota = float(input("Digite uma nota para remover: "))

remover_nota(notas, nota)

print("Notas atualizadas:", notas)

resultado = media_notas(notas)

print("Média:", resultado)
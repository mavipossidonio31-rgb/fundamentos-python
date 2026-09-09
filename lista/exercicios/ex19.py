
def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)


def adicionar_varias(notas, novas):
    notas.extend(novas)


def remover_nota(notas, nota):
    notas.remove(nota)


def remover_ultima(notas):
    return notas.pop()


def encontrar_nota(notas, nota):
    return notas.index(nota)


def quantidade_notas(notas):
    return len(notas)

notas = [7.5, 6.0, 8.5, 9.0, 5.5]

print("Notas:", notas)

adicionar_nota(notas, 8.0)
print("Depois de adicionar:", notas)

inserir_nota(notas, 10.0, 2)
print("Depois de inserir:", notas)

adicionar_varias(notas, [6.5, 7.0])
print("Depois de adicionar várias:", notas)

remover_nota(notas, 5.5)
print("Depois de remover:", notas)

nota = remover_ultima(notas)
print("Nota removida:", nota)

posicao = encontrar_nota(notas, 8.5)
print("Posição da nota 8.5:", posicao)

quantidade = quantidade_notas(notas)
print("Quantidade de notas:", quantidade)


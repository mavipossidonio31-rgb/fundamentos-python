def remover_item(itens, posicao):
    item = itens.pop(posicao)
    return item


itens = ["Lápis", "Caneta", "Caderno", "Borracha"]

posicao = int(input("Digite a posição que deseja remover: "))


print("Item removido:", resultado)
print("Lista:", itens)

resultado = remover_item(itens, posicao)
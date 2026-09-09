def mostra_nome(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["renan", "moises", "fabiana", "manu", "lu"]

mostra_nome(lista_de_nomes)


# Adicionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)


adicionar_nome(lista_de_nomes, "isabel")


# Adicionando novo nome em uma posição específica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} da lista: {nomes}")


adicionar_nome_posicao(lista_de_nomes, "rogerio", 2)


# Juntando duas listas
def juntar_nome(nomes, novo_nomes):
    nomes.extend(novo_nomes)
    print(nomes)


outra_lista = ["joao", "maria"]

juntar_nome(lista_de_nomes, outra_lista)


# Removendo nome pelo valor
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"{nome} foi removido da lista: {nomes}")


remover_nome_pelo_valor(lista_de_nomes, "renan")


# Removendo nome pelo índice
def remover_nome_pelo_indice(nomes, posicao):
    if 0 <= posicao < len(nomes):
        nome = nomes.pop(posicao)
        print(f"O nome {nome} foi removido da lista: {nomes}")
    else:
        print("Essa posição não existe na lista")


remover_nome_pelo_indice(lista_de_nomes, 2)


# Descobrindo a posição (índice) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome in nomes:
        posicao = nomes.index(nome)
        print(f"O nome {nome} está na posição: {posicao}")
    else:
        print(f"O nome {nome} não foi encontrado na lista")


encontrar_posicao_pelo_valor(lista_de_nomes, "manu")


# Contando elementos da lista
def quantidade_de_nomes(nomes):
    total = len(nomes)
    print(f"A lista possui {total} nomes.")


quantidade_de_nomes(lista_de_nomes)

#ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenada = sorted(lista_de_nomes)
    print(f"a lista ordenada e {lista_de_nomes_ordenada}")

ordenar_nomes(lista_de_nomes)

#operacao matematicas
#calcular media
def calcular_media(notas)
  total=sum(notas)
  quantidades=len(notas)
  media=total/quantidades
  print(f"a media das notas e {media}")

  notas




  #lista de de lista
  def adicionar_produto():
    produto = input(produtos,produto):
    produto.append(produto)
    print(f'minhas lista de produtos : {produtos[0]}')

    lista_produtos=[
        ["arroz",2,32.00],
        ["feijao",3,8.50]
    ]
    novo_produto = ["cafe",2,28.00]
    adicionar_produto(lista_produtos,novo_produto)









def procurar_palavra(texto, palavra):
    posicao = texto.find(palavra)

    if posicao == -1:
        print("palavra não encontrada!")
    else:
        print("a palavra começa na posição", posicao)


texto = input("digite um texto: ")
palavra = input("digite uma palavra: ")

procurar_palavra(texto, palavra)
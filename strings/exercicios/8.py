def verificar_palavra(texto, palavra):

    if palavra in texto:
        print("palavra encontrada!")
    else:
        print("palavra não encontrada!")


texto = input("digite um texto: ")
palavra = input("digite uma palavra: ")

verificar_palavra(texto, palavra)
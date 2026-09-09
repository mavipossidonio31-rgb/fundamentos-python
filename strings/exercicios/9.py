def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)


texto = input("digite um texto: ")

print("quantidade de palavras:", contar_palavras(texto))
def substituir_palavra(frase, palavra_1, palavra_2):
    return frase.replace(palavra_1, palavra_2)


frase = input("digite uma frase: ")
palavra_1 = input("digite a palavra antiga: ")
palavra_2 = input("digite a palavra nova: ")

print(substituir_palavra(frase, palavra_1, palavra_2))
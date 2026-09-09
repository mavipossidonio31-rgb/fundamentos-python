def contar_letra(frase, letra):
    return frase.count(letra)


frase = input("digite uma frase: ")
letra = input("digite uma letra: ")

print("a letra aparece", contar_letra(frase, letra), "vezes.")
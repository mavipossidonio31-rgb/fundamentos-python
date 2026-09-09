def validar_telefone(numeros):

    if numeros.isdigit():
        print("número de telefone válido!")
    else:
        print("número inválido! Digite somente números.")


telefone = input("digite seu telefone: ")

validar_telefone(telefone)
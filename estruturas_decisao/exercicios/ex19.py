def numero():
    n = int(input("digite um número: "))

    if n > 0:
        positivo_negativo = "positivo"
    elif n < 0:
        positivo_negativo = "negativo"
    else:
        positivo_negativo = "zero"

    if n % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"

    print("Número:", n)
    print("Classificação:", positivo_negativo, "e", par_impar)


numero()
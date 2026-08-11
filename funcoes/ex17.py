
def trocar_valores():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    print("\nAntes:")
    print("A =", A)
    print("B =", B)

    aux = A
    A = B
    B = aux

    print("\nDepois:")
    print("A =", A)
    print("B =", B)


trocar_valores()
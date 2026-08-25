def eh_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def mostrar_primos(inicio, fim):
    for i in range(inicio, fim + 1):
        if eh_primo(i):
            print(i)


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

mostrar_primos(inicio, fim)
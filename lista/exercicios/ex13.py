def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    cliente = fila.pop(0)
    return cliente


fila = []

while True:

    cliente = input("Digite o nome do cliente ou 0 para parar: ")

    if cliente == "0":
        break

    adicionar_cliente(fila, cliente)


print("Fila:", fila)

if len(fila) > 0:

    cliente = atender_cliente(fila)

    print("Cliente atendido:", cliente)

print("Fila final:", fila)
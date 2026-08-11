
def consumo():
    distancia = float(input("Digite a distância percorrida: "))
    combustivel = float(input("Digite a quantidade de combustível: "))

    consumo = distancia / combustivel

    print("Consumo médio:", consumo, "km/L")

consumo()
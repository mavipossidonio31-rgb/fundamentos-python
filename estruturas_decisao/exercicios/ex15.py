def verificar_velocidade():
    velocidade = float(input("digite a velocidade do veículo (km/h): "))

    if velocidade <= 60:
        print("velocidade permitida")
    elif velocidade <= 80:
        print("atenção: velocidade acima do permitido")
    else:
        print("multa por excesso de velocidade")


verificar_velocidade()
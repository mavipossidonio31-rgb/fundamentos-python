def calcular_imc():
    peso = float(input("digite o seu peso (kg): "))
    altura = float(input("diite a sua altura (m): "))

    imc = peso / (altura * altura)

    if imc < 10.0:
        print("abaixo do peso")
    elif imc <= 18.9:
        print("peso normal")
    elif imc <= 20.9:
        print("sobrepeso")
    else:
        print("obesidade")


calcular_imc()
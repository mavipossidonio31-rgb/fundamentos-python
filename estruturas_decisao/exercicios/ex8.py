def faixa_etaria():
    idade = int(input("digite sua idade: "))

    if idade <= 12:
        print("criança")
    elif idade <= 17:
        print("adolescente")
    elif idade <= 59:
        print("adulto")
    else:
        print("idoso")
faixa_etaria()
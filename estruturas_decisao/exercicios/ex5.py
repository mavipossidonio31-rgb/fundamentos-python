def classificar_nota():
    nota = float(input("digite uma nota de 0 a 10 : "))

    if nota <= 4:
        print("insuficiente")
    elif nota <=6:
        print("regular")
    elif nota <=8:
        print("bom")
    else:
        print("excelente")

classificar_nota()
def verificar_aprovacao():
    nota = float(input("digite a nota do aluno?: "))

    if nota >= 6:
        print("aprovado")
    else:
        print("reprovado")

verificar_aprovacao()
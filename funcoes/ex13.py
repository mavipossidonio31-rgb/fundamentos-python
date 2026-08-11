
def comissao():
    salario = float(input("Digite o salário fixo: "))
    vendas = float(input("Digite o valor das vendas: "))
    percentual = float(input("Digite a comissão (%): "))

    salario_final = salario + (vendas * percentual / 100)

    print("Salário final:", salario_final)

comissao()
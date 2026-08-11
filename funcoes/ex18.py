
def valor_prestacao():
    produto = float(input("Digite o valor do produto: "))
    parcelas = int(input("Digite a quantidade de parcelas: "))

    valor = produto / parcelas

    print("O valor de cada parcela é: R$", valor)


valor_prestacao()
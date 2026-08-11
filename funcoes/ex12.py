def desconto():
    preco = float(input("Digite o preço do produto: "))
    percentual = float(input("Digite o desconto (%): "))

    valor_final = preco - (preco * percentual / 100)

    print("Valor final:", valor_final)

desconto()
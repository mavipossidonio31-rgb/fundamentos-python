def calculadora():
    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))
    operacao = input("digite a operação (+, -, * ou /): ")

    if operacao == "+":
        print("resultado:", num1 + num2)
    elif operacao == "-":
        print("resultado:", num1 - num2)
    elif operacao == "*":
        print("resultado:", num1 * num2)
    elif operacao == "/":
        print("resultado:", num1 / num2)
    else:
        print("operação inválida!")


calculadora()
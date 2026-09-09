from calculadora import somar, subtrair, multiplicar, dividir


def executar_calculadora():
    aluno = {}

    operacoes = {
        "1": somar,
        "2": subtrair,
        "3": multiplicar,
        "4": dividir
    }

    while True:
        print("========calculadora=======\n")
        print("*******escollha uma opçao:*******\n")
        print("1 - somar")
        print("2 - subtrair")
        print("3 - multiplicar")
        print("4 - dividir")
        print("0 - sair")

        opcao = input("escolha uma opçao: ")

        if opcao == "0":
            print("-------calculadora encerrada--------")
            break

        if opcao not in operacoes:
            print("Opção inválida. Tente novamente.\n")
            continue

        # Estes inputs e cálculos estavam muito para dentro (indentados errados)
        numero1 = float(input("informe o primeiro valor: "))
        numero2 = float(input("informe o segundo valor: "))

        funcao = operacoes[opcao]
        resultado = funcao(numero1, numero2)

        print(f'resultado: {resultado}\n')


# Chamada da função para o programa rodar
executar_calculadora()
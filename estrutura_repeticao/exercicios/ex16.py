def validar_senha(senha_correta):
    tentativas = 0

    while tentativas < 3:
        senha = input("digite a senha: ")

        if senha == senha_correta:
            print("Acesso permitido")
            return

        print("senha incorreta")
        tentativas = tentativas + 1

    print("acesso bloqueado")


validar_senha("1234")
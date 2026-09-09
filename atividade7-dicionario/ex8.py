def sistema_login():
    sistema = {
        "usuario": "admin",
        "senha": "123"
    }

    login_digitado = input("Digite o usuário: ")
    senha_digitada = input("Digite a senha: ")

    if login_digitado == sistema["usuario"] and senha_digitada == sistema["senha"]:
        print("Login realizado com sucesso! Bem-vindo(a).")
    else:
        print("Usuário ou senha incorretos. Acesso negado.")


sistema_login()
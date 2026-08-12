def aluno_aprovado():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    media = (nota_1 + nota_2) / 2

    if media >= 6:
        print("aluno aprovado!")

    elif media >=5 and media <=6:

        print("aluno de recuperacao!")
    else:
        print("aluno reprovado!")

#aluno_aprovado()


def login():
    e_mail = "maria.vitoria"
    senha= "1234"
    codigo_secreto = "#456@"

    e_mail_input = input("Digite seu e-mail: ")
    senha_input = input("Digite sua senha: ")

    if e_mail_input == e_mail and senha_input == senha:
        print("usuario logado!")
        acessar_admin = input("deseja acessar usuario? [S/N]")
        if acessar_admin == "S":
            codigo_secreto_input = input("Digite seu codigo secreto: ")
            if codigo_secreto_input == codigo_secreto:
                print("acesso adm liberado")
            else:
                print("codigo secreto incorreto!")
        elif acessar_admin == "n":
            print("ok vc acessou como usuario comum")

        else:
               print("email ou senha incorreto!")
login()
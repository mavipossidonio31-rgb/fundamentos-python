def cadastro_notas():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    aluno["media"] = media

    print(f"\nO aluno {aluno['nome']} ficou com a media: {aluno['media']:.2f}")


cadastro_notas()
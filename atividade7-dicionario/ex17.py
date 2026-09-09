def cadastro_varios_alunos():
    alunos = []

    print("Cadastre 5 alunos:")
    for i in range(5):
        print(f"\n--- Aluno {i + 1} ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        nota = float(input("Nota: "))


        aluno = {
            "nome": nome,
            "idade": idade,
            "nota": nota
        }


        alunos.append(aluno)

    print("\n--- listas de todos os alunos   ---")
    for a in alunos:
        print(f"Nome: {a['nome']} | Idade: {a['idade']} | Nota: {a['nota']}")


cadastro_varios_alunos()
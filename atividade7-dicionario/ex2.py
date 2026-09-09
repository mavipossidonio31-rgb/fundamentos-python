def alterar_aluno():
    aluno = {
        "nome": "Carlos",
        "idade": 17,
        "telefone": "88888-8888",
        "endereço": "Av. Central, 45",
        "cidade": "Campinas",
        "nota": 8.5,
        "turma": "A",
        "curso": "Informática"
    }

    print("--- antes da alteracao  ---")
    print("Idade:", aluno["idade"])
    print("Cidade:", aluno["cidade"])

    aluno["idade"] = 18
    aluno["cidade"] = "Santos"

    print("\n--- DEPOIS DA ALTERAÇÃO ---")
    print("Idade:", aluno["idade"])
    print("Cidade:", aluno["cidade"])


alterar_aluno()
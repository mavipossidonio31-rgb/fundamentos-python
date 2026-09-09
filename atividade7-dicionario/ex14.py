def calcular_notas_aluno():
    aluno = {
        "nome": "Carlos",
        "notas": [8.0, 7.5, 9.0]
    }

    print("Nome do aluno:", aluno["nome"])
    print("Todas as notas:", aluno["notas"])
    print("Maior nota:", max(aluno["notas"]))
    print("Menor nota:", min(aluno["notas"]))


    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"Média das notas: {media:.2f}")


calcular_notas_aluno()
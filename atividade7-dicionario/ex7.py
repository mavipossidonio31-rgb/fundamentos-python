def verificar_aprovacao():
    aluno = {
        "nome": "Juliana",
        "media": 7.0,
        "frequencia": 80
    }

    # Verificando se passou por média (>= 6) E frequência (>= 75)
    if aluno["media"] >= 6 and aluno["frequencia"] >= 75:
        print(f"Parabéns {aluno['nome']}, você foi APROVADO(A)!")
    else:
        print(f"Que pena {aluno['nome']}, você foi REPROVADO(A).")


verificar_aprovacao()
def cadastro_filmes():
    filme = {
        "titulo": "Aventura no Espaço",
        "ano": 2022,
        "genero": "Ficção",
        "notas": []
    }

    print(f"Cadastrando notas para o filme: {filme['titulo']}")

    for i in range(5):
        nota = float(input(f"Digite a {i + 1}ª nota (de 0 a 10): "))
        filme["notas"].append(nota)

    media = sum(filme["notas"]) / len(filme["notas"])

    print(f"\nFilme: {filme['titulo']}")
    print(f"Notas cadastradas: {filme['notas']}")
    print(f"Média final do filme: {media:.2f}")


cadastro_filmes()
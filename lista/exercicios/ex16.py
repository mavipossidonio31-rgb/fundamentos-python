def criar_ranking(pontuacoes):
    pontuacoes = sorted(pontuacoes, reverse=True)
    return pontuacoes


pontuacoes = [100, 250, 80, 300, 150]

ranking = criar_ranking(pontuacoes)

print("Ranking:", ranking)
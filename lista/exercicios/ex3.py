def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)


convidados = ["Maria", "João"]

print("Lista no começo:", convidados)

novos_convidados = ["Pedro", "Ana", "Lucas"]

adicionar_convidados(convidados, novos_convidados)

print("Lista no fim:", convidados)
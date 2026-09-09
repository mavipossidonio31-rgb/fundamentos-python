def verificar_extensao(nome_arquivo):

    if nome_arquivo.endswith(".pdf"):
        print("arquivo válido.")
    else:
        print("arquivo inválido.")


arquivo = input("digite o nome do arquivo: ")

verificar_extensao(arquivo)
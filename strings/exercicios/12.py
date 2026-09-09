def separar_dados(dados):
    partes = dados.split(",")

    print("nome:", partes[0])
    print("idade:", partes[1])
    print("profissão:", partes[2])
    print("cidade:", partes[3])


dados = "João,40,Desenvolvedor,Piracicaba"

separar_dados(dados)
def sistema_produtos():
    produtos = []

    while True:
        print("\n===== sistema de produtos =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar estoque")
        print("5 - Remover produto")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque inicial: "))

            produto = {"nome": nome, "preco": preco, "estoque": estoque}
            produtos.append(produto)
            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            if len(produtos) == 0:
                print("Nenhum produto cadastrado.")
            else:
                print("\n--- PRODUTOS CADASTRADOS ---")
                for p in produtos:
                    print(f"Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")

        elif opcao == "3":
            busca = input("Digite o nome do produto que deseja buscar: ")
            encontrado = False
            for p in produtos:
                if p["nome"].lower() == busca.lower():
                    print(f"Encontrado -> Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado.")

        elif opcao == "4":
            busca = input("Digite o nome do produto para alterar o estoque: ")
            encontrado = False
            for p in produtos:
                if p["nome"].lower() == busca.lower():
                    qtd = int(input("Digite a quantidade a somar (positivo) ou subtrair (negativo): "))
                    p["estoque"] += qtd
                    print(f"Estoque atualizado! Novo estoque de {p['nome']}: {p['estoque']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado.")

        elif opcao == "5":
            busca = input("Digite o nome do produto que deseja remover: ")
            removido = False
            for p in produtos:
                if p["nome"].lower() == busca.lower():
                    produtos.remove(p)
                    print("Produto removido com sucesso!")
                    removido = True
                    break
            if not removido:
                print("Produto não encontrado.")

        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


sistema_produtos()
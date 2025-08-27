inventario = []  # lista que vai armazenar os itens como dicionários

while True:
    print("\n===== CONTROLE DE INVENTÁRIO =====")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar inventário")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade: "))
        inventario.append({"nome": nome, "quantidade": quantidade})
        print(f"✅ Item '{nome}' adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do item a remover: ")
        encontrado = False
        for item in inventario:
            if item["nome"].lower() == nome.lower():
                inventario.remove(item)
                print(f"❌ Item '{nome}' removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print(f"⚠️ Item '{nome}' não encontrado no inventário.")

    elif opcao == "3":
        if inventario:
            print("\n📦 Inventário Atual:")
            for item in inventario:
                print(f"- {item['nome']} (Quantidade: {item['quantidade']})")
        else:
            print("📭 Inventário vazio.")

    elif opcao == "4":
        print("👋 Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")

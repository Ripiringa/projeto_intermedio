total = 0
opcao = 0

qtd = {
    "Café": 0,
    "Chá": 0,
    "Sandes": 0,
    "Bolo": 0,
    "Água": 0,
    "Sumo": 0
}

while opcao != 10:
    print("===== MENU CAFÉ DIGITAL =====")
    print("1 - Café (1.20 €)")
    print("2 - Chá (1.00 €)")
    print("3 - Sandes (2.50 €)")
    print("4 - Bolo (1.80 €)")
    print("5 - Água (0.80 €)")
    print("6 - Sumo (1.50 €)")
    print("7 - Adicionar produto")
    print("8 - Ver carrrinho de compras")
    print("9 - Ver total")
    print("10 - Sair")
    print("=" * 29)

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            quantidade = int(input("Quantos deste produto deseja: "))
            qtd["Café"] += quantidade
            total += 1.20 * quantidade
            print(f"{quantidade} Café(s) adicionado ao carrinho de compras.")
        case 2:
            quantidade = int(input("Quantos deste produto deseja: "))
            qtd["Chá"] += quantidade
            total += 1.00 * quantidade
            print(f"{quantidade} Chá(s) adicionado ao carrinho de compras.")
        case 3:
            quantidade = int(input("Quantos deste produto deseja: "))
            qtd["Sandes"] += quantidade
            total += 2.50 * quantidade
            print(f"{quantidade} Sandes adicionada ao carrinho de compras.")
        case 4:
            quantidade = int(input("Quantos deste produto deseja: "))
            qtd["Bolo"] += quantidade
            total += 1.80 * quantidade
            print(f"{quantidade} Bolo(s) adicionado ao carrinho de compras.")
        case 5:
            quantidade = int(input("Quantos deste produto deseja: "))
            qtd["Água"] += quantidade
            total += 0.80 * quantidade
            print(f"{quantidade} Água(s) adicionada ao carrinho de compras.")
        case 6:
            quantidade = int(input("Quantos deste produto deseja: "))
            qtd["Sumo"] += quantidade
            total += 1.50 * quantidade
            print(f"{quantidade} Sumo(s) adicionado ao carrinho de compras.")
        case 7:
            nome = input("Nome do novo produto: ")
            quantidade = int(input("Quantos deste produtos deseja: "))
            preco = float(input("Preço (€): "))
            total += preco * quantidade
            if nome in qtd:
                qtd[nome] += quantidade
            else:
                qtd[nome] = quantidade
            print(f"'{nome}' adicionado ao carrinho de compras.")
        case 8:
            print("===== RESUMO DA COMPRA ATÉ AO MOMENTO =====")
            for produto, quantidade in qtd.items():
                if quantidade > 0:
                    print(f"{produto}: {quantidade}")
            print(f"Total até ao momento {total:.2f} €")
            print("=" * 43)
        case 9:
            for produto, quantidade in qtd.items():
                if quantidade > 0:
                    print(f"{produto}: {quantidade}")
            break
        case 10:
            print("A sair do programa...")
        case _:
            print("Opção inválida. Tente novamente.")

if total > 10:
    total *= 0.9
    print("Desconto de 10% aplicado!")

print(f"Total a pagar: {total:.2f} €")
print("Obrigado pela sua compra!")
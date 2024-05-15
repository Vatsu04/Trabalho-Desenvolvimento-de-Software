import funcoes as func

while True:
    func.menu()
    opcao = int(input("Digite o número correspondente para selecionar uma opção do menu: "))

    if opcao == 0:
        break

    elif opcao == 1:
        print("Matemática financeira é um ramo da matemática que estuda o comportamento do dinheiro ao longo do tempo.")
        print("Ela é aplicada em diversas áreas, como finanças pessoais, investimentos, empréstimos, entre outros.")

    elif opcao == 2:
        func.submenu_porcentagem()

    elif opcao == 3:
        func.submenu_lucro_prejuizo()

    elif opcao == 4:
        func.submenu_juros()

    elif opcao == 5:
        func.submenu_desconto_acrescimo

    elif opcao == 6:
        func.submenu_roi()

    elif opcao == 7:
        func.submenu_valor_presente_liquido()

    elif opcao == 8:
        func.submenu_taxa_interna_retorno()

  

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

        
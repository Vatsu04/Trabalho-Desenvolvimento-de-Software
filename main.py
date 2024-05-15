import funcoes as func

def menu():
    print('')
    print('1 - O que é matemática financeira e para que serve.')
    print('2 - Cálculo de porcentagem.')

    print('3 - Cálculo de lucro')
    print('4 - Cálculo de prejuízo')  

    print('5 - Calcular Montante')
    print('6 - Calcular Juros Simples')
    print('7 - Calcular Juros Compostos')

    print('8 - Calcular Desconto')
    print('9 - Calcular Acrescimo')
    print('0 - Sair')
    print('')



while True:
    menu()
    opcao = int(input("Digite o número correspondente para selecionar uma opção do menu: "))

    if opcao == 0:
        break

    elif opcao == 1:
        print("Matemática financeira é um ramo da matemática que estuda o comportamento do dinheiro ao longo do tempo.")
        print("Ela é aplicada em diversas áreas, como finanças pessoais, investimentos, empréstimos, entre outros.")

    elif opcao == 2:
        valor = float(input("Digite o valor: "))
        percentual = float(input("Digite a porcentagem: "))
        resultado = func.porcentagem(valor, percentual)
        print(f"{percentual}% de {valor} é {resultado}.")

    elif opcao == 3:
        lucro_total = float(input("Digite o lucro total: "))
        custo = float(input("Digite o custo: "))
        valor_venda = float(input("Digite o valor da venda: "))
        lucro_calculado, percentual_lucro = func.lucro(lucro_total, custo, valor_venda)
        print(f"Lucro: {lucro_calculado}")
        print(f"Percentual de lucro: {percentual_lucro}%")

    elif opcao == 4:
        prejuizo_total = float(input("Digite o prejuízo total: "))
        custo = float(input("Digite o custo: "))
        valor_venda = float(input("Digite o valor da venda: "))
        prejuizo_calculado, percentual_prejuizo = func.prejuizo(prejuizo_total, custo, valor_venda)
        print(f"Prejuízo: {prejuizo_calculado}")
        print(f"Percentual de prejuízo: {percentual_prejuizo}%")

    elif opcao == 5:
        capital = float(input("Digite o capital inicial: "))
        taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
        tempo = int(input("Digite o tempo (em anos): "))
        montante = func.calcular_montante(capital, taxa_juros, tempo)
        print(f"O montante é: {montante}")

    elif opcao == 6:
        valor_principal = float(input("Digite o valor principal: "))
        taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
        tempo = int(input("Digite o tempo (em anos): "))
        montante = func.juros_simples(valor_principal, taxa_juros, tempo)
        print(f"O montante com juros simples é: {montante}")

    elif opcao == 7:
        valor_principal = float(input("Digite o valor principal: "))
        taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
        tempo = int(input("Digite o tempo (em anos): "))
        montante = func.juros_compostos(valor_principal, taxa_juros, tempo)
        print(f"O montante com juros compostos é: {montante}")

    elif opcao == 8:
        preco_inicial = float(input("Digite o preço inicial: "))
        taxa_desconto = float(input("Digite a taxa de desconto (em porcentagem): "))
        desconto, preco_novo = func.calcular_desconto(preco_inicial, taxa_desconto)
        print(f"O desconto é: {desconto}")
        print(f"O preço com desconto é: {preco_novo}")

    elif opcao == 9:
        preco_inicial = float(input("Digite o preço inicial: "))
        taxa_acrescimo = float(input("Digite a taxa de acréscimo (em porcentagem): "))
        acrescimo, preco_novo = func.calcular_acrescimo(preco_inicial, taxa_acrescimo)
        print(f"O acréscimo é: {acrescimo}")
        print(f"O preço com acréscimo é: {preco_novo}")

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

        
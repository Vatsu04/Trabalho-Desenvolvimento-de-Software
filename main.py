import funcoes as func
import cadastro as cad





def main():
    while True:
        func.menu()
        try:
            opcao = int(input("Digite o número correspondente para selecionar uma opção do menu: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if opcao == 0:
            break

        elif opcao == 1:
            print("Matemática financeira é um ramo da matemática que estuda o comportamento do dinheiro ao longo do tempo.")
            print("Ela é aplicada em diversas áreas, como finanças pessoais, investimentos, empréstimos, entre outros.")

        elif opcao == 2:
            func.submenu_porcentagem(logged_in)
        
        elif opcao == 3:
            func.submenu_lucro_prejuizo(logged_in)

        elif opcao == 4:
            func.submenu_juros(logged_in)

        elif opcao == 5:
            func.submenu_desconto_acrescimo(logged_in)

        elif opcao == 6:
            func.submenu_roi(logged_in)

        elif opcao == 7:
            func.submenu_valor_presente_liquido(logged_in)

        elif opcao == 8:
            func.submenu_taxa_interna_retorno(logged_in)

        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")



if __name__ == "__main__":
    while True:
        possui_cadastro = input("Possui cadastro (s/n)? ")
        if possui_cadastro.lower() == 's':
            logged_in = func.log_in()

        elif possui_cadastro.lower() == 'n':
            logged_in = func.cadastro()
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")
            continue

        if logged_in:
            
            main()
            break

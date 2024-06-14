import funcoes as func
import cadastro as cad
import login

def main():
    accessed_submenus = set()
    summary = ""

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
            if "Porcentagem" not in accessed_submenus:
                summary += "Porcentagem"
                accessed_submenus.add("Porcentagem")
            func.submenu_porcentagem()

        elif opcao == 3:
            if "Lucro e Prejuízo" not in accessed_submenus:
                summary += "Lucro e Prejuízo"
                accessed_submenus.add("Lucro e Prejuízo")
            func.submenu_lucro_prejuizo()

        elif opcao == 4:
            if "Juros" not in accessed_submenus:
                summary += "Juros"
                accessed_submenus.add("Juros")
            func.submenu_juros()

        elif opcao == 5:
            if "Desconto e Acréscimo" not in accessed_submenus:
                summary += "Desconto e Acréscimo"
                accessed_submenus.add("Desconto e Acréscimo")
            func.submenu_desconto_acrescimo()

        elif opcao == 6:
            if "ROI" not in accessed_submenus:
                summary += "ROI"
                accessed_submenus.add("ROI")
            func.submenu_roi()

        elif opcao == 7:
            if "Valor Presente Líquido" not in accessed_submenus:
                summary += "Valor Presente Líquido"
                accessed_submenus.add("Valor Presente Líquido")
            func.submenu_valor_presente_liquido()

        elif opcao == 8:
            if "Taxa Interna de Retorno" not in accessed_submenus:
                summary += "Taxa Interna de Retorno"
                accessed_submenus.add("Taxa Interna de Retorno")
            func.submenu_taxa_interna_retorno()

    print("Summary of accessed submenus:", summary)

def log_in():
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    login_successful, result = login.login(username, password)
    if login_successful:
        print(f"Login bem-sucedido! ID do usuário: {result}")
        return True
    else:
        print(f"Falha no login: {result}")
        return False

if __name__ == "__main__":
    while True:
        possui_cadastro = input("Possui cadastro (s/n)? ")
        if possui_cadastro.lower() == 's':
            logged_in = log_in()
        elif possui_cadastro.lower() == 'n':
            logged_in = cad.cadastro()
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")
            continue

        if logged_in:
            main()
            break

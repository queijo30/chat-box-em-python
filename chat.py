import re

def mostrar_menu():
    print("Bem-vindo à Pizzaria!")
    print("1. Opções de Pizza")
    print("2. Colocar Endereço")
    print("3. Pagamento e Finalização da Compra")
    print("0. Sair")

def opcoes_pizza():
    print("Opções de Pizza:")
    print("1. Margherita")
    print("2. Pepperoni")
    print("3. Quatro Queijos")
    print("4. Portuguesa")
    print("0. Voltar ao Menu Principal")

def colocar_endereco():
    while True:
        endereco = input("Por favor, insira seu endereço (somente números): ")
        if re.match("^[0-9]+$", endereco):
            print(f"Endereço '{endereco}' salvo com sucesso!")
            return endereco
        else:
            print("Endereço inválido. Por favor, insira apenas números.")

def pagamento_finalizacao():
    print("Opções de Pagamento:")
    print("1. Pix")
    print("2. Cartão")
    escolha_pagamento = input("Escolha uma opção de pagamento: ")

    if escolha_pagamento == "1":
        print("Gerando código Pix...")
        print("Código Pix: 1234567890")
        print("A pizza está a caminho!")
        return "Pix", "1234567890"
    elif escolha_pagamento == "2":
        print("1. Débito")
        print("2. Crédito")
        escolha_cartao = input("Escolha uma opção de cartão: ")
        if escolha_cartao == "1":
            numero_cartao = input("Insira o número do cartão de débito: ")
            print(f"Pagamento com cartão de débito {numero_cartao} realizado com sucesso!")
            print("A pizza está a caminho!")
            return "Débito", numero_cartao
        elif escolha_cartao == "2":
            numero_cartao = input("Insira o número do cartão de crédito: ")
            print(f"Pagamento com cartão de crédito {numero_cartao} realizado com sucesso!")
            print("A pizza está a caminho!")
            return "Crédito", numero_cartao
    else:
        print("Opção de pagamento inválida.")
        return None, None

def salvar_informacoes(pizza, endereco, pagamento, detalhes_pagamento):
    with open("info.py", "w") as file:
        file.write(f"pizza = '{pizza}'\n")
        file.write(f"endereco = '{endereco}'\n")
        file.write(f"pagamento = '{pagamento}'\n")
        file.write(f"detalhes_pagamento = '{detalhes_pagamento}'\n")

def main():
    pizza_escolhida = False
    endereco_inserido = False
    pizza = ""
    endereco = ""
    pagamento = ""
    detalhes_pagamento = ""

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            opcoes_pizza()
            escolha_pizza = input("Escolha uma pizza: ")
            if escolha_pizza in ["1", "2", "3", "4"]:
                print("Opção escolhida")
                pizza_escolhida = True
                pizza = escolha_pizza
                endereco = colocar_endereco()
                endereco_inserido = True
                pagamento, detalhes_pagamento = pagamento_finalizacao()
                salvar_informacoes(pizza, endereco, pagamento, detalhes_pagamento)
                break
            elif escolha_pizza == "0":
                continue
            else:
                print("Opção inválida. Por favor, tente novamente.")
        elif escolha == "2":
            if pizza_escolhida:
                endereco = colocar_endereco()
                endereco_inserido = True
            else:
                print("Por favor, escolha uma pizza primeiro.")
        elif escolha == "3":
            if pizza_escolhida and endereco_inserido:
                pagamento, detalhes_pagamento = pagamento_finalizacao()
                salvar_informacoes(pizza, endereco, pagamento, detalhes_pagamento)
                break
            else:
                print("Por favor, escolha uma pizza e insira o endereço primeiro.")
        elif escolha == "0":
            print("Obrigado por usar a Pizzaria! Até a próxima.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()


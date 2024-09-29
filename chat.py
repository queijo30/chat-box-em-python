import re
import sqlite3

# Funções para interagir com o banco de dados
def inicializar_banco():
    conn = sqlite3.connect('pizzaria.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pizza TEXT,
            endereco TEXT,
            pagamento TEXT,
            detalhes_pagamento TEXT,
            refrigerante TEXT
        )
    ''')
    conn.commit()
    return conn

def salvar_informacoes(conn, pizza, endereco, pagamento, detalhes_pagamento, refrigerante):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (pizza, endereco, pagamento, detalhes_pagamento, refrigerante)
        VALUES (?, ?, ?, ?, ?)
    ''', (pizza, endereco, pagamento, detalhes_pagamento, refrigerante))
    conn.commit()

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

def opcoes_refrigerante():
    print("Opções de Refrigerante:")
    print("1. Coca-Cola")
    print("2. Fanta")
    print("3. Sprite")
    print("4. Água")
    print("0. Nenhum")

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
        numero_cartao = input("Insira o número do cartão: ")
        if escolha_cartao == "1":
            print(f"Pagamento com cartão de débito {numero_cartao} realizado com sucesso!")
        elif escolha_cartao == "2":
            print(f"Pagamento com cartão de crédito {numero_cartao} realizado com sucesso!")
        print("A pizza está a caminho!")
        return "Cartão", numero_cartao
    else:
        print("Opção de pagamento inválida.")
        return None, None

def main():
    conn = inicializar_banco()
    pizza_escolhida = False
    endereco_inserido = False
    pizza = ""
    endereco = ""
    pagamento = ""
    detalhes_pagamento = ""
    refrigerante = ""

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
                refrigerante_opcao = opcoes_refrigerante()
                pagamento, detalhes_pagamento = pagamento_finalizacao()
                salvar_informacoes(conn, pizza, endereco, pagamento, detalhes_pagamento, refrigerante)
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
                refrigerante = input("Escolha um refrigerante: ")
                pagamento, detalhes_pagamento = pagamento_finalizacao()
                salvar_informacoes(conn, pizza, endereco, pagamento, detalhes_pagamento, refrigerante)
                break
            else:
                print("Por favor, escolha uma pizza e insira o endereço primeiro.")
        elif escolha == "0":
            print("Obrigado por usar a Pizzaria! Até a próxima.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

    conn.close()

if __name__ == "__main__":
    main()

## Criação de um Sistema Bancário para o Desafio do Bootcamp Suzano - Python Developer da DIO

from datetime import datetime, timedelta, time, date

menu = """
Seja Bem-Vindo(a)
[D] - Depositar
[S] - Sacar
[E] - Extrato Bancário
[Q] - Sair
"""

LIMITE_SAQUES = 3
LIMITE_TRANSACOES_DIARIA = 10
valor_limite = 500
saldo = 0
cheque_especial = 0
extrato = ""
numero_saques = 0
numero_transacoes = 0

while True:
    opcao = input(menu)
    numero_transacoes += 1

    if numero_transacoes <= LIMITE_TRANSACOES_DIARIA:

        if opcao == "D":
            valor_deposito = float(input("Informe o Valor do Deposito: "))

            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Transação Número: {numero_transacoes}\nValor depositado de: R$ {valor_deposito:.2f}\nDeposito realizado em {datetime.now()}\n\n"

            else:
                print("Operação falhou! Valor informado é incorreto.")
        
        elif opcao == "S":
            valor_saque = float(input("Informe o Valor para saque: "))

            excedeu_saques = numero_saques >= LIMITE_SAQUES
            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > valor_limite

            if excedeu_saques:
                print("Operação Falhou! Número de saques excedido no dia.")
            
            elif excedeu_saldo:
                print("Operação Falhou! Você não tem saldo suficiente.")
            
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite diário.")
            
            elif valor_saque > 0:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Transação Número: {numero_transacoes}\nSaque efetuado de: R$ {valor_saque:.2f}\nDeposito realizado em {datetime.now()}\n\n"

            else:
                print("Operação falhou! Informe um valor válido.")
        
        elif opcao == "E":
            print("\n=================== EXTRATO ===================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print("-------------------------------------------------")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print(f"\nCheque Especial: R$ {cheque_especial:.2f}")
            print("=================================================")
        
        elif opcao == "Q":
            break

        else:
            print("Operação Inválida. Por favor selecione a Operação desejada.")     

    else:
        print("Operação Inválida. Limite de transação diária excecida.")
        print("Para sua Segurança, retorne outro dia.")
        print("Obrigado!")
        break

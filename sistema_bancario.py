import os

menu = f"""\033[36m

  ____                                   __  __       _   _                    
 |  _ \                                 |  \/  |     | | | |                   
 | |_) | __ _ _ __   ___ ___    ______  | \  / | __ _| |_| |__   ___ _   _ ___ 
 |  _ < / _` | '_ \ / __/ _ \  |______| | |\/| |/ _` | __| '_ \ / _ \ | | / __|
 | |_) | (_| | | | | (_| (_) |          | |  | | (_| | |_| | | |  __/ |_| \__ \\
 |____/ \__,_|_| |_|\___\___/           |_|  |_|\__,_|\__|_| |_|\___|\__,_|___/
\033[m
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=> """

MENSAGEM_FALHA = f"\033[31m[FALHA] -\033[m" 
MENSAGEM_SUCESSO = f"\033[32m[SUCESSO] -\033[m" 
MENSAGEM_CONTINUE = f"\n\033[37mPressione <Enter> para voltar ao menu...\033[m"

TAMANHO_CELULAS = 14

TITULO_1 = "Operação".center(TAMANHO_CELULAS)
TITULO_2 = "Número".center(TAMANHO_CELULAS)
TITULO_3 = "Valor".center(TAMANHO_CELULAS)
TITULO_4 = "Saldo".center(TAMANHO_CELULAS)

extrato = f"\n|{TITULO_1}|{TITULO_2}|{TITULO_3}|{TITULO_4}|\n\n"

saldo = 0
limite = 500
numero_deposito = 0
numero_saque = 0
LIMITE_SAQUES = 3

os.system("clear") # Limpa a tela no inicia do programa

while True:
    # Solicita o comando:
    opcao = input(menu)

    # Operação de depósito:
    if opcao == "1":

        print() # Quebra de linha

        # Validando o depósito:
        while True:
            valor_deposito = float(input(f"Digite o valor de depósito \033[31m(0 cancela)\033[m: R$ "))

            # Condições.:
            cancelar_deposito = valor_deposito == 0
            deposito_invalida = valor_deposito < 0

            # Cancela a operação
            if cancelar_deposito:
                print(f"\n{MENSAGEM_FALHA} Depósito cancelado!")
                input(MENSAGEM_CONTINUE)
                os.system("clear")
                break  

            # Solicita que usuário entre com o valor novamente por deposito inválido!
            elif deposito_invalida:
                print(f"\n{MENSAGEM_FALHA} Digite um valor positivo ou zero para cancelar!", end="\n\n");
                continue

            # Computa o depósito
            numero_deposito += 1
            saldo += valor_deposito

            # Adiciona no extrato
            menssagem_operacao_deposito = str("Depósito").center(TAMANHO_CELULAS)
            menssagem_operacao_deposito = f"\033[34m{menssagem_operacao_deposito}\033[m"

            mensagem_numero_deposito = str(numero_deposito).center(TAMANHO_CELULAS)
            mensagem_numero_deposito = f"\033[34m{mensagem_numero_deposito}\033[m"

            mensagem_valor_deposito = f"+ R${valor_deposito:<.2f}".center(TAMANHO_CELULAS)
            mensagem_valor_deposito = f"\033[32m{mensagem_valor_deposito}\033[m"

            mensagem_saldo_deposito = f"R${saldo:<.2f}".center(TAMANHO_CELULAS)
            mensagem_saldo_deposito = f"\033[32m{mensagem_saldo_deposito}\033[m"

            extrato = extrato.__add__(f"|{menssagem_operacao_deposito}|{mensagem_numero_deposito}|{mensagem_valor_deposito}|{mensagem_saldo_deposito}|\n")
            
            # Finaliza a operação
            print(f"\n{MENSAGEM_SUCESSO} Depósito realizado!")
            input(MENSAGEM_CONTINUE)
            os.system("clear")
            break

    # Operação de saque:             
    elif opcao == "2":

        print() # Quebra de linha

        # Validando o saque:
        if numero_saque < LIMITE_SAQUES:

            while True:
                valor_saque = float(input(f"Digite o valor de saque \033[31m(0 cancela)\033[m: R$ "))
                
                # Condições.:
                cancelar_saque = valor_saque == 0
                saque_invalido = valor_saque < 0
                saque_insuficiente = valor_saque > saldo
                limite_saque_insuficiente = valor_saque > limite
                
                # Cancela a operação
                if cancelar_saque:
                    print(f"\n{MENSAGEM_FALHA} Saque cancelado!", end="\n\n")
                    input(MENSAGEM_CONTINUE)
                    os.system("clear")
                    break

                # Solicita que usuário entre com o valor novamente por saque inválido!
                elif saque_invalido:
                    print(f"\n{MENSAGEM_FALHA} Digite um valor positivo ou zero para cancelar!", end="\n\n")
                    continue
                
                # Solicita que usuário entre com o valor novamente por saldo insuficiente
                elif saque_insuficiente:
                    print(f"\n{MENSAGEM_FALHA} Saldo insuficiente!", end="\n\n")
                    continue

                # Solicita que usuário entre com o valor novamente por limite de saque insuficiente
                elif limite_saque_insuficiente:
                    print(f"\n{MENSAGEM_FALHA} Seu limite de saque é: R${limite:.2f}", end="\n\n")
                    continue
                
                # Valor válido - Computa o saque
                numero_saque += 1
                saldo -= valor_saque

                menssagem_saque = f"\033[31m- R${valor_saque:<11.2f}\033[m"

                # Adiciona no extrato
                menssagem_operacao_saque = str("Saque").center(TAMANHO_CELULAS)
                menssagem_operacao_saque = f"\033[33m{menssagem_operacao_saque}\033[m" 
                
                mensagem_numero_saque = str(numero_saque).center(TAMANHO_CELULAS)
                mensagem_numero_saque = f"\033[33m{mensagem_numero_saque}\033[m"

                mensagem_valor_saque = f"- R${valor_saque:<.2f}".center(TAMANHO_CELULAS)
                mensagem_valor_saque = f"\033[31m{mensagem_valor_saque}\033[m"

                mensagem_saldo_saque = f"R${saldo:<.2f}".center(TAMANHO_CELULAS)
                mensagem_saldo_saque = f"\033[31m{mensagem_saldo_saque}\033[m"

                extrato = extrato.__add__(f"|{menssagem_operacao_saque}|{mensagem_numero_saque}|{mensagem_valor_saque}|{mensagem_saldo_saque}|\n")

                print(f"\n{MENSAGEM_SUCESSO} Saque realizado com sucesso!")
                input(MENSAGEM_CONTINUE)
                os.system("clear")
                break

        else:
            # O limite de saques por dia foi atingido!
            print(f"\n{MENSAGEM_FALHA} Você atingiu seu limite de saques diários!")
            input(MENSAGEM_CONTINUE)
            os.system("clear")

    # Operação de exiber extrato:
    elif opcao == "3":
        
        print() # Quebra de linha

        # Imprimindo o Extrato da conta
        print(extrato)
        print(f"Saldo da conta = \033[35mR${saldo:.2f}\033[m")

        input(MENSAGEM_CONTINUE)
        os.system("clear")

    # Operação de sair do sistema
    elif opcao == "0":

        print() # Quebra de linha

        # Imprime o título da operação
        print(f"Saindo\n")
        break

    # Comando inválido
    else:
        print(f"\n{MENSAGEM_FALHA} Operação inválida, por favor selecione novamente a operação desejada.")
        input(MENSAGEM_CONTINUE)
        os.system("clear")

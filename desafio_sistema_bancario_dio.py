menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input('Digite o valor a ser depositado: '))
        
        if deposito > 0:
            saldo += deposito
            print(f'Depósito de R$ {deposito:.2f} realizado com sucesso.')
            extrato += f'Depósito: R$ {deposito:.2f}\n'
        else:
            print('Valor inválido. Por favor, tente novamente.')

    elif opcao == "s":
        saque = float(input('Digite o valor a ser sacado: '))
        
        if numero_saques >= limite_saques:
            print('Você excedeu o limite diário de saques. Por favor, tente novamente amanhã.')
        
        elif saque > saldo:
            print('Você não possui saldo suficiente para a operação. Por favor, tente novamente.')
        
        elif saque > limite:
            print('O valor inserido está acima do permitido por saque. Por favor, tente novamente.')
        
        elif saque > 0:
            saldo -= saque
            print(f'Saque de R$ {saque:.2f} realizado com sucesso.')
            extrato += f'Saque: R$ {saque:.2f}\n'
        
        else:
            print('Valor inválido. Por favor, tente novamente.')
        

    elif opcao == "e":
        print('####### EXTRATO #######')
        
        if len(extrato) == 0:
            print('Não houve operações no período.')
        
        else:
            print(extrato)
        
        print('#######################')
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
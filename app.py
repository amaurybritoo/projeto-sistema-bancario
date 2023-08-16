import datetime
print('sistema bancario\n'.upper())

menu = """
(L) Saldo
(D) Deposito
(E) Extrato
(S) Saque
(F) Sair

Digite a operação que deseja realizar: """

saldo = 0
limite = float(500)
Extrato = []

numero_saque = 0
limite_saque = 3

data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # DATA atual e hora

while True:
    opcao = input(menu)

    if opcao.upper() == 'L':
        print(f'\nSaldo em conta R$: {saldo:.2f}')

    elif opcao.upper() == 'D':
        valor_deposito = float(input('valor do deposito: R$ '))
        if valor_deposito > 0:
            saldo += valor_deposito
            Extrato.append(f'Data: {str(data)} + Deposito: R$ {valor_deposito:.2f}')
            print('operação efetuada com sucesso!\n')
        else:
            print("O valor do deposito tem que ser acima de R$o,oo Reais!!!\n")

    elif opcao.upper() == 'S':
    
        if numero_saque <= limite_saque:
            valor_saque = float(input('Valor de saque: R$ '))
            numero_saque += 1
            if valor_saque > 0:
                if valor_saque <= limite and valor_saque <= saldo:
                    Extrato.append(f'Data: {str(data)} - Saque: R$ {valor_saque:.2f}')
                    print('operação efetuada com sucesso!\n')
                    saldo -= valor_saque                   
                else:
                    print(f'O limite de saque é de {saldo:.2f}')
            else:
                print('Você deve informar um valor de saque valido!!!')
        else:
           print('Você não pode mais efetuar saques, escedeu o seu limite diário de saques(3 saques diarios).')

    elif opcao.upper() == 'E':
        print(Extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao.upper() == "F":
        break

    else:
        print("Operação inválida, por favor digite uma opção válida.")
print("Volte sempre e conte com os nossos serviços!")

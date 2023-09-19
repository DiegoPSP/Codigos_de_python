print("1 para conta_Normal;\n2 para conta_universitária;\n3 para conta_especial\n")
opcao = int(input("Digite: "))

conta_Normal = opcao == 1
conta_universitaria = opcao == 2
conta_especial = opcao == 3

valor = int(input("Digite o valor que deseja sacar: "))
saldo = 2000
saque = valor
cheque_especial = 450

if conta_Normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, tente novamente ou entre em contato com seu gerente!")

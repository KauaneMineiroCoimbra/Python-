 #-----------------------------------------------------------
    #exercicio 06 
saldo = 0

while True:
    print("\n1. Consultar Saldo\n2. Depositar\n3. Sacar\n0. Sair")
    op = int(input("Opção: "))

    if op == 0:
        break

    elif op == 1:
        print(f"Saldo atual: R$ {saldo}")

    elif op == 2:
        valor = float(input("Depósito: "))
        if valor < 0:
            print("Valor inválido")
        else:
            saldo += valor

    elif op == 3:
        valor = float(input("Saque: "))
        if valor < 0:
            print("Valor inválido")
        elif valor > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor

    else:
        print("Opção inválida")
        
       
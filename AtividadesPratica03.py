#exercicio. 01 
print("--- Tabuada ---- ")
def tabuada(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")

n = int(input("digite um numero: "))
tabuada(n)

 #-----------------------------------------------------------
  #exercicio 02
print(" ---- Calculadora ---")
def calcular(op, a, b):
    if op == 1:
     return print(f"Resultado: {a} + {b}= {a+b}")
    elif op == 2:
     return print(f"Resultado: {a} - {b}= {a-b}")
    elif op == 3:
     return print(f"Resultado: {a} * {b}= {a*b}")
    elif op == 4:
        if b == 0: 
         return print("Divisão por zero nao permitida")
        return print(f"Resultado: {a} / {b}= {a/b}")
    else: 
        return print("Opção invalida")
    
    while true:
        print("\n1. Somar\n2.Subtrair\n3. Multiplicar\n 4.dividir\n0.sair")
        op = int(input("Opção: "))
        
        if op == 0:
            print("Fim.")
            break
        
        if op < 1 or op > 4:
            print("Opção invalida")
            continue
        
        a = float(input("numero 1: "))
    b = float(input("numero 2: "))
    
    print(calcular(op,a,b))
    
    #-----------------------------------------------------------
    #exercicio 03 
    print("Controle de temperatura")
    maior = None
    menor = None 
    
    while True:
     t = float(input("Temperatura: "))
     if t == 0: 
         break
     if t < -50 or t > 60:
        print("Temperatura inválida")
        continue

    if maior is None or t > maior:
        maior = t
    if menor is None or t < menor:
        menor = t
        print(f"Maior temperatura: {maior}") 
        print(f"Menor temperatura: {menor}")
        
        #-----------------------------------------------------------
    #exercicio 04
    #Cixa de um mercado
    total = 0

while True:
    valor = float(input("Valor: "))

    if valor == 0:
        break

    if valor < 0:
        print(f"Valor inválido: {valor}")
        continue

    total += valor

parcelas = int(input("Parcelas: "))

if parcelas <= 1:
    print(f"Pagamento à vista: R$ {total}")
else:
    print(f"Total da compra: R$ {total}")
    print(f"Parcelado em {parcelas}x de R$ {total/parcelas:.2f}")
    
        #-----------------------------------------------------------
    #exercicio 05   
    original = input("Palavra: ")
soletrada = ""

while True:
    letra = input("Letra: ")

    if letra == "0":
        break

    soletrada += letra

print(f"Palavra original: {original}")
print(f"Palavra soletrada: {soletrada}")
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
 #-----------------------------------------------------------
    #exercicio 07
    n = int(input("Número: "))

if n <= 0:
    print("Parâmetro inválido")
else:
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i

    print(f"O fatorial de {n} é {resultado}.")
    
 #-----------------------------------------------------------
    #exercicio 08
   
    pos = int(input("Posição: "))

if pos <= 0:
    print("Valor inválido")
elif pos == 1 or pos == 2:
    print(1)
else:
    a, b = 1, 1
    for i in range(3, pos + 1):
        a, b = b, a + b

    print(f"O valor na posição {pos} é {b}")
    
 #-----------------------------------------------------------
#exercicio 09
base = int(input("Base: "))
altura = int(input("Altura: "))

if base <= 0 or altura <= 0:
    print("Retângulo inválido")
else:
    for i in range(altura):
        for j in range(base):
            print("*", end=" ")
        print()
        
 #-----------------------------------------------------------
#exercicio 10
altura = int(input("Altura: "))

if altura <= 0:
    print("Triângulo inválido")
else:
    for i in range(1, altura + 1):
        for j in range(i):
            print("*", end=" ")
        print()
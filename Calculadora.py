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
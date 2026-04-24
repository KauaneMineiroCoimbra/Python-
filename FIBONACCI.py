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
        
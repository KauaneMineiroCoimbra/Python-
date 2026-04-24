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
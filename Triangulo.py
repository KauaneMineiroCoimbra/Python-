#exercicio 10
altura = int(input("Altura: "))

if altura <= 0:
    print("Triângulo inválido")
else:
    for i in range(1, altura + 1):
        for j in range(i):
            print("*", end=" ")
        print()
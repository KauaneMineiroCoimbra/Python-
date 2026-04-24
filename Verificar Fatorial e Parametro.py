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
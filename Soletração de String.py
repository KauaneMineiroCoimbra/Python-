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
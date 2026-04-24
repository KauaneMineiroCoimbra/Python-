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
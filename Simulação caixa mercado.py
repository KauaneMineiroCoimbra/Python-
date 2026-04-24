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
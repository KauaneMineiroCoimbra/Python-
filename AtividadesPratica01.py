
# Atividade 1 - Apresentar estudante
nome = input("Digite seu nome: ")
curso = input("Digite seu curso: ")
semestre = input("Digite seu semestre atual: ")
hobby = input("Digite seu hobby favorito: ")

print("Prazer, eu sou a " + nome + "!")
print("Atualmente estou no " + semestre + "º semestre de " + curso + " e meu hobby favorito é " + hobby + ".\n")

# Atividade 2 - Churrasco
print("Atividade 2: Churrasco de Domingo")
pessoas = int(input("Quantas pessoas vão participar? "))

# Quantidade por pessoa em kg
carne_por_pessoa = 0.3
linguica_por_pessoa = 0.2
frango_por_pessoa = 0.15

# Preços por kg
preco_carne = 50
preco_linguica = 28
preco_frango = 22

# Calcular quantidade total
carne_total = pessoas * carne_por_pessoa
linguica_total = pessoas * linguica_por_pessoa
frango_total = pessoas * frango_por_pessoa

# Calcular custo
custo_carne = carne_total * preco_carne
custo_linguica = linguica_total * preco_linguica
custo_frango = frango_total * preco_frango
custo_total = custo_carne + custo_linguica + custo_frango

# Valor por pessoa
valor_por_pessoa = custo_total / pessoas

print("Quantidades:")
print("Carne: " + str(carne_total) + " kg, Linguiça: " + str(linguica_total) + " kg, Frango: " + str(frango_total) + " kg")
print("Custo total: R$", custo_total)
print("Cada pessoa deve pagar: R$", round(valor_por_pessoa, 2), "\n")

# Atividade 3 - Média de Notas
print("Atividade 3: Média de Notas")
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print("O(A) estudante " + nome_aluno + " ficou com média " + str(round(media,1)) + "\n")

# Atividade 4 - Compra no Exterior
print("Atividade 4: Compra no Exterior")
valor_real = float(input("Digite o valor em reais:.2f"))
cotacao_dolar = 5.42
valor_dolar = valor_real / cotacao_dolar

print("Valor em real R$ " + str(valor_real))
print("Valor em dólar $ " + str(round(valor_dolar,2)) + "\n")


# Atividade 5 - Compra Online
print("Atividade 5: Compra Online")
nome_cliente = input("Digite seu nome: ")
valor_compra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o desconto em %: "))

valor_final = valor_compra * (1 - desconto / 100)

print("Olá " + nome_cliente + ", sua compra de R$ " + str(valor_compra) + " foi confirmada!")
print("Foi aplicado um desconto de " + str(desconto) + "%")
print("O total final ficou em R$ " + str(round(valor_final,2)) + "\n")


# Atividade 6 - IMC
print("Atividade 6: IMC")
nome_pessoa = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)
print(nome_pessoa + ", seu IMC é de " + str(round(imc,2)) + "\n")

# Atividade 7 - Leitura de Livro
print("Atividade 7: Você lê rápido?")
nome_leitor = input("Digite seu nome: ")
livro = input("Digite o nome do livro: ")
paginas = int(input("Digite o total de páginas: "))
tempo_segundos = float(input("Tempo de leitura por página em segundos: "))

tempo_total_horas = (paginas * tempo_segundos) / 3600
print(nome_leitor + ", você finalizará o livro " + livro + " em aproximadamente " + str(round(tempo_total_horas,2)) + " horas.\n")


# Atividade 8 - Açaiteria
print("Atividade 8: Açaiteria")
acai_p = int(input("Quantos Açaí pequeno? "))
acai_m = int(input("Quantos Açaí médio? "))
acai_g = int(input("Quantos Açaí grande? "))
desconto_acai = float(input("Desconto em %: "))

preco_p = 13.5
preco_m = 15
preco_g = 17.5

total_acai = (acai_p*preco_p + acai_m*preco_m + acai_g*preco_g)
total_desconto = total_acai * (1 - desconto_acai/100)

print("Seu pedido foi registrado:")
print("- Açaí P:", acai_p)
print("- Açaí M:", acai_m)
print("- Açaí G:", acai_g)
print("Desconto de", desconto_acai, "% aplicado")
print("Total R$", round(total_desconto,2), "\n")



# Atividade 9 - Piloto Kart
print("Atividade 9: Piloto Kart")
tamanho_pista = float(input("Tamanho da pista em metros: "))
voltas = int(input("Número de voltas: "))
tempo_primeira = float(input("Tempo da primeira volta em segundos: "))

distancia_total = (tamanho_pista * voltas)/1000
previsao_min = (tempo_primeira * voltas)/60

print("Distância total: " + str(round(distancia_total,2)) + " km")
print("Previsão de conclusão: " + str(round(previsao_min,1)) + " minutos\n")


# Atividade 10 - Meta Pessoal
print("Atividade 10: Meta Pessoal")
meta = input("Descrição da meta: ")
valor_meta = float(input("Valor necessário: "))
salario = float(input("Salário mensal: "))
despesas = float(input("Despesas mensais: "))

saldo = salario - despesas
reserva = saldo * 0.3
valor_mensal_meta = saldo - reserva
meses = valor_meta / valor_mensal_meta

print("Meta:", meta, "(R$ " + str(valor_meta) + ")")
print("Salário: R$ " + str(salario) + ", Despesas: R$ " + str(despesas))
print("Saldo após despesas: R$ " + str(round(saldo,2)))
print("Reserva fixa (30%): R$ " + str(round(reserva,2)))
print("Valor disponível para a meta: R$ " + str(round(valor_mensal_meta,2)) + " por mês")
print("Prazo estimado: " + str(round(meses,2)) + " meses")
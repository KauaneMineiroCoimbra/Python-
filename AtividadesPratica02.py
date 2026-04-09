#exercicio 01- orçamneto Familiar 
ganhos = float(input("Digite os ganhos: "))
gastos = float(input("Digite os gastos: "))

if ganhos >= gastos:
  print("Você está dentro do orçamento!")
else:
  print("Você está fora do orçamento! Não gaste mais!")
  
  #exercicio 02- sémaforo
  cor = input("Digite a cor do semáforo: ").lower()

if cor == "vermelho":
    print("Espere")
elif cor == "verde":
    print("Atravesse")
else:
    print("Farol inoperante")
    
    #exercicio03- dia por extenso
dia = int(input("Digite o número do dia (0-6): "))

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

if 0 <= dia <= 6:
    print(dias[dia])
else:
    print("Dia da semana inválido")
    
#exercicio 04-sorveteria em promoção
gramas = float(input("Digite o peso em gramas: "))

if gramas <= 0:
    print("Peso inválido")
else:
    preco_100g = 3.5
    if gramas >= 1000:
        preco_100g -= 0.5
    
    total = (gramas / 100) * preco_100g
    print(f"O total é R$ {total:.2f}")

#exercicio 05- Boletim do aluno
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
faltas = int(input("Faltas: "))

media = (n1 + n2 + n3) / 3

if n1 < 0 or n2 < 0 or n3 < 0 or n1 > 10 or n2 > 10 or n3 > 10 or faltas < 0:
    print("Parâmetros inválidos")
else:
    print(f"Média: {media:.1f}")
    
    if faltas > 4:
     print("Situação: Reprovado por Falta")
    elif media == 0:
      print("Situação: Desistente")
    elif media < 6:
        print("Situação: Recuperação")
    elif media < 8:
        print("Situação: Aprovado")
    else:
        print("Situação: Aprovado com sucesso")
        
#exercicio 06- qual a cor ?
c1 = input("Cor 1: ").lower()
c2 = input("Cor 2: ").lower()

primarias = ["vermelho", "azul", "amarelo"]

if c1 not in primarias or c2 not in primarias:
    print("Apenas cores primárias são aceitas.")
else:
    if (c1 == "vermelho" and c2 == "azul") or (c1 == "azul" and c2 == "vermelho"):
        print("Roxo")
    elif (c1 == "vermelho" and c2 == "amarelo") or (c1 == "amarelo" and c2 == "vermelho"):
        print("Laranja")
    elif (c1 == "azul" and c2 == "amarelo") or (c1 == "amarelo" and c2 == "azul"):
        print("Verde")
    else:
        print("Mesma cor")
        
#exercicio 07- nota de corte
nota = float(input("Nota do candidato: "))
corte = float(input("Nota de corte: "))
min_aprov = float(input("Nota mínima: "))

if nota < corte:
    print("Situação candidato: Reprovado")
elif nota >= min_aprov:
    print("Situação candidato: Aprovado")
else:
    print("Situação candidato: Lista de Espera")

#exercicio 08= calculadora por menu
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Operação: ").lower()

if op in ["1", "soma"]:
    print(a + b)
elif op in ["2", "subtração"]:
    print(a - b)
elif op in ["3", "multiplicação"]:
    print(a * b)
elif op in ["4", "divisão"]:
    print(a / b)
elif op in ["5", "resto"]:
    print(a % b)
elif op in ["6", "potência"]:
    print(a ** b)
else:
    print("Operação não suportada")
    
    #exercicio 09= mensalidade universidade
curso = input("Curso: ").upper()
isento = input("Isento (sim/não): ").lower()
desconto = float(input("Desconto (%): "))

tabela = {
    "SI": 900,
    "ADS": 750,
    "CS": 1150,
    "EC": 1300,
    "ES": 950
}

if curso not in tabela:
    print("Curso não encontrado")
else:
    valor = tabela[curso]
    
    if isento == "sim":
        valor = 0
    else:
        valor -= valor * (desconto / 100)
    
    print(f"Valor da mensalidade: R$ {valor:.2f}")
    
#exercicio 10- ingressos de cinema
inteiras = int(input("Qtd inteiras: "))
meias = int(input("Qtd meias: "))
dia = input("Dia da semana: ").lower()
nacional = input("Filme nacional (sim/não): ").lower()

preco = 28.5

if nacional == "sim":
    total = (inteiras + meias) * 5
elif dia == "quarta-feira":
    total = (inteiras + meias) * 14.5
else:
    total = inteiras * preco + meias * (preco / 2)

print(f"Total a pagar: R$ {total:.2f}")
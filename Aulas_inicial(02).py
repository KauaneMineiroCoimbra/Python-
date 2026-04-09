#aula01- trila 02 
#apresentação trilha 02 - processamento e saida

#demonstrando sobre como fazer o modelo condicional
#o modelo sequencial e condicional e 
#entrada
#processamento
#saida

#valor da condicional: if else, else, if 
# if= se | if else= se não 
#----------------------------------


#aula 02- trilha 02
#a origem da inteligencia

# --- Exemplo 1: Caixa Eletrônico
#saldo_em_conta = 500.00
#valor_saque = 100.00
# O programa chega no ponto de decisão
# PERGUNTA: saldo_em_conta >= valor_saque ?
# SE (a resposta for Verdadeira):
#Liberar o dinheiro 1
#saldo_em_conta = saldo_em_conta - valor_saque
# SENÃO (se a resposta for Falsa):
#Exibir "Saldo Insuficiente"
#print("#" * 30)
# --- Exemplo 2: Análise de Dados para Relatórios
# Em Python, isso é extremamente comum!
#meta_de_vendas = 10000.00
#vendas_do_mes = 12500.00

#trilha 02- aula 03 modelo de algoritmo 
#print ("---iniciando uma emissão de nota fiscal----")
#print("2. Listando produtos e quantidades.")
#print("3. Calculando o valor subtotal da venda.")

# --- PARTE 2: MODELO CONDICIONAL
#print("\n[CONDICIONAL] Analisando impostos ... ")
#produto_eh_servico = False # Simulando que é um produto

# O programa faz uma pergunta e escolhe um caminho
# SE (produto_eh_servico for Verdadeiro):
# print("-> Aplicando imposto ISS ... ")
# SENÃO:
# print("-> Produto não é servico, ISS nao aplicavel.")

#------------------------------------------
#-------------------------------------------

#aula 04- comparacoes booleanas;
#divida_cliente_A = 500.0
#divida_cliente_B = 1500.0
#divida_cliente_C = 1000.0
#divida_cliente_D = 1000.0

#A==B (E IGUAL?)
#A>B( A E MAIOR QUE B)
#A<B( A MENOR QUE B )
#A <=B(A E MENOR OU IGUAL A B)

#teste_1 = (divida_cliente_A == divida_cliente_B)
#print(teste_1)

#teste_2 = (divida_cliente_A < divida_cliente_B)
#print(teste_1)

#teste_3 = (divida_cliente_A <= divida_cliente_B)
#print(teste_1)


#----------------------------------------------
#----------------------------------------------
#AULA 05- COMBINAÇÃO DE COMPARAÇÃO 
#regras de negocios 
# RENDA_MINIMA = 4.000
# SCORE_MINIMO = 600

# print(" --- Analise de Credito Simplificada --- ")
# print(f"Regra: Renda > R$ {RENDA_MINIMA} AND Score > {SCORE_MINIMO}")

# # Cliente 1: Carlos
# renda_carlos = 5500.0
# score_carlos = 720

# # Cliente 2: Juliana
# renda_juliana - 6000.0
# score_juliana = 550

# aprovado_carlos = (renda_carlos > RENDA_MINIMA) and (score_carlos > SCORE_MINIMO)
# print(f"Analise Carlos (Renda: R$ {renda_carlos :.2f}), Score: {score_carlos}: Aprovado? {aprovado_carlos}")

# aprovado_juliana = (renda_juliana > RENDA_MINIMA) and (score_carlos > SCORE_MINIMO)
# print(f"Analise juliana (Renda: R$ {renda_carlos:.2f}), Score: {score_juliana}: Aprovada? {aprovado_juliana}")


# elif (salario <= 2826.65):
# print("Faixa 2: Aliquota de IR é de 7.5%.")
# elif (salario <- 3751.05):
# print("Faixa 3: Aliquota de IR é de 15%")
# elif (salario <= 4664.68):
# print("Faixa 4: Aliquota de IR é de 22.5%")
# else:
# print("Faixa 5: Aliquota de IR é de 27.5%")

# print(f"Analisando o salário de: R$ {salario :. 2f}")
# # Inicio da cadeia de decisão
# if (salario <= 2259.20):
# print("Faixa 1: Isento de IR.")

# renda = 6008.0
# idade - 25
# historico_bom True

# print(" --- Analise de Credito Especial --- ")
# # VERSÃO 1 - Aninhada (dificil de ler)
# print("\nAnalisanda com if's aninhados ... ")
# if renda > 5000.0:
# # A renda e boa, agora vamos checar a idade
# if idade > 21:
# # A idade tambem e bos, agora precisamos verificar o historico
# if historico_bom:
# print("Resultado: Credito APROVADO.")
# print(" Resultado: Negado (historio de pagamento ruim).")

# else:
# print("Resultado: Negado (idade abaixo do minino).")

# else:
# print("Resultado: Negado (renda insuficiente).")


# # VERSÃO 1 - Aninhada (dificil de lar)
# print("\nAnalisando com if's aninhados ... ")
# if renda > 5000.8:
# # A renda é boa, agora vamos checar a idade
# if idade > 21:
# # A idade tambom é boa, agora procisamos verificar o historico
# if historico_bom:
  #---------------------------------------------------------------------
  
# print("Resultado: Credito APROVADO.")
# print(" Resultado: Negado (histerio de pagamento ruim).")
# else:
# print("Resultado: Negado (idade abaixo do minino).")
# else
# print("Resultado: Negado (renda insuficiente).")
#----------------------------------------------------------------------------

# # VERSÃO 2: Simplificada com 'and' (codigo limpo)
# print("\nAnalisando con operador logico 'and" ... ")
# if (renda > 5000.0) and (idade > 21) and (historico_bom):
# # Se TODAS as tres condicoes forem True, entra aqui
# print("Resultado: Credito APROVADO.")
# else:
# Se QUALOUER UMA das tres condicoes for False. entra aqui

#aula 10 e 11
#-----------------------------------------------------------------
# renda = 6000.0
# idade = 25
# historico_bom = True

# print(f" --- Analise de Credito Especial --- ")

# # VERSÃO 1 - Aninhada (dificil de ler)
# #-------------------------------------------------------------------
# print(f"\nAnalisando com if's aninhados ... ")
# if renda > 5000.0:
# # A renda e boa, agora vamos checar a idade
# if idade > 21:
# # A idade tambem é boa, agora precisamos verificar o histórico
# if historico_bom
# print(f"Resultado: Crédito APROVADO.")
# else
# print(f" Resultado: Negado (historio de pagamento ruim).")
# else
# print("Resultado: Negado (idade abaixo do minimo).")
# else
# print("Resultado: Negado (renda insuficiente).")

# # VERSÃO 2: Simplificada com 'and' (codigo limpo)
# #-------------------------------------------------------------------
# print("\nAnalisando com operador logico 'and' ... ")

# if (renda > 5000.0) and (idade > 21) and (historico_bom):
# # Se TODAS as tres condicões forem True, entra aqui
# print("Resultado: Credito APROVADO.")
# else:
# # Se QUALQUER UMA das três condições for False, entra aqui
# print("Resultado: Crédito NEGADO.")

# # --- Versão 1: Bloco if-else tradicional
# if vendas > 1000.0:
# bonus_padrao = 500.0
# else:
# bonus_padrao = 100.0

# print(f"Com if-else, para vendas de R$ {vendas :. 2f}, o bônus é: R$ {bonus_padrao :. 2f}")

# # --- Versão 2: Expressão condicional Ternária
# # Lê-se: "500 SE vendas > 1000.0 else 100"
# bonus_ternario = 500 if vendas > 1000.0 else 100

# print(f"Com ternário, para vendas de R$ {vendas :. 2f}, o bônus é: R$ {bonus_ternario :. 2f}")
# #aula 12
# #------------------------------------------------------------------------

# #Expressão
# 5+3 
# media >= 7.0
# bonus = 500 if vendas > 1000.0 else 100

# #comando
# nome= "ana"
# print("ola, mundo")
# if valor > 10: #faça algo
# else: #faça outra coisa

# def cliente_esta_inadimplente(dias_atraso):
# print(f" --- (EXPRESSÃO SENDO AVALIADA: Verificando status com {dias_atraso} dia de atraso)    ----")
# return dias_atraso > 0 

# # Dados dos Clientes
# dias_cliente_a = 0
# dias_cliente_b = 35

# print("Analisando Cliente A:")
# if cliente_esta_inadimplente(dias_cliente_a):
# print("Ação: Enviar e-mail de cobranca. \n")
# else:
# print("Ação: Enviar e-mail de agradecimento por estar em dia. \n")

# print("Analisando Cliente B:")
# if cliente_esta_inadimplente(dias_cliente_b):
# print("Ação: Enviar e-mail de cobrança. \n")
# else:
# print("Ação: Enviar e-mail de agradecimento por estar em dia. \n")






##AULA '13- COMANDO SWITCH
# Simula a opção que o usuário digitou
# opcao 3

# print(f"Opção selecionada: {opcao}")
# print("-

# # O comando 'if-elif-else' avalia a variavel 'opcao'
# if opcao == 1:
# print("Açao: Executando a rotina de CADASTRO de funcionario.")
# elif opcao == 2:
# print("Açao: Executando a rotina de EDICÃO de dados.")
# elif opcao == 3:
# print("Ação: Executando a rotina de EXCLUSÃO de funcionário.")
# elif opcao == 4:
# print("Ação: Executando a rotina de CONSULTA de dados.")
# else: # Este bloco funciona como o 'case ' (default)
# print("Ação: Opcão invalida! Por favor, tente novamente.")

# print("
# print("Operação finalizada.")



# Questão
# —
# Considere as afirmativas sobre operadores relacionais:
# I. Operadores como >, <, >=, <=, == e != são utilizados para comparar valores.  
# II. O resultado de uma expressão com operador relacional é sempre um valor booleano (True ou False).  
# III. Operadores relacionais não podem ser utilizados com variáveis, apenas com valores fixos.  

# Assinale a alternativa correta:
# (1 Ponto)

# Apenas I está correta

# Apenas I e III estão corretas

# Apenas I e II estão corretas

# Apenas II e III estão corretas

# I, II e III estão corretas
# 2
# Questão
# —
# Considere as afirmativas sobre operadores lógicos:
# I. O operador `and` (E lógico) retorna verdadeiro apenas quando ambas as condições são verdadeiras.  
# II. O operador `or` (OU lógico) retorna verdadeiro quando pelo menos uma condição é verdadeira.  
# III. O operador `not` (NÃO lógico) inverte o valor lógico de uma condição.  

# Assinale a alternativa correta:
# (1 Ponto)

# Apenas I está correta

# Apenas I e III estão corretas

# Apenas I e II estão corretas

# Apenas II e III estão corretas

# I, II e III estão corretas
# 3
# Questão
# —
# Considere as afirmativas sobre o tipo booleano:
# I. O tipo boolean possui apenas dois valores possíveis: `True` e `False`.
# II. Valores boolean são frequentemente utilizados em estruturas condicionais.  
# III. O tipo booleano pode armazenar qualquer valor numérico.  

# Assinale a alternativa correta:
# (1 Ponto)

# Apenas I está correta

# Apenas I e II estão corretas

# Apenas I e III estão corretas

# Apenas II e III estão corretas

# I, II e III estão corretas
# 4
# Questão
# —
# Sobre o papel das condições em um algoritmo, é correto afirmar:


# (1 Ponto)

# Elas são usadas apenas para imprimir mensagens

# Elas substituem variáveis

# Elas só funcionam em linguagens compiladas

# Elas determinam quais partes do código serão executadas

# Elas não influenciam o resultado do algoritmo
# 5
# Questão
# —

# Considere as afirmações sobre condições:
# I. Uma condição pode envolver comparações entre variáveis.  
# II. Condições podem ser simples ou compostas.  
# III. Condições não podem utilizar valores booleanos diretamente.

# Assinale a alternativa correta:

# (1 Ponto)

# Apenas I está correta

# Apenas I e II estão corretas

# Apenas I e III estão corretas

# Apenas II e III estão corretas

# I, II e III estão corretas
# 6
# Questão
# —

# Sobre a estrutura completa (if, elif, else), considere:
# I. O `if` é sempre o primeiro bloco da estrutura.  
# II. O `elif` é opcional e pode aparecer várias vezes.  
# III. O `else` é opcional e executa quando nenhuma condição anterior é verdadeira.

# Assinale a alternativa correta:

# (1 Ponto)

# Apenas I está correta

# Apenas I e II estão corretas

# Apenas I e III estão corretas

# Apenas II e III estão corretas

# I, II e III estão corretas
# 7
# Questão - Análise de Código
# —

# Analise o código, qual será a saída? 
# (1 Ponto)


# Pode dirigir

# Não pode dirigir

# true

# false

# Nenhuma saída
# 8
# Questão - Precedência de Operadores
# —

# Analise o código, qual será a saída? 
# (1 Ponto)


# 7

# 8

# 9

# 10

# 0
# 9
# Questão - Análise de Código
# —

# Analise o código, qual será a saída?

# Considere a entrada da senha sendo, "admin".
# (1 Ponto)


# Bem-vindo

# Acesso negado

# Carlos

# Erro

# Nenhuma saída
# 10
# Questão - Análise de erro
# —

# Analise o código, possui algum erro?
# (1 Ponto)


# Condição deve retornar booleano em Python

# Os blocos estão inconsistentes

# O print está incorreto

# A variável nota deveria ser float

# Outro erro
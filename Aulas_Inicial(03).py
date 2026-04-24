
#aula 01
# Abordagem Manual (Modelo Sequencial/Condicional)
# print("Contagem: 1")
# print("Contagem: 2")
# print("Contagem: 3")
# print("Contagem: 4")
# print("Contagem: 5")

# # Abordagem Iterativa
# contador = 1

# while contador <= 5:
# print(f"Contagem: {contador}")
# contador += 1 # Incremento: essencial para não termos um loop infinito


#------------------------------------------------------------------

#Aula 02
# CALCULO E CADASTRO SEM REPETIÇÃO (Abordagem Limitada)

# print(" --- Sistema de Cadastro de Produtos --- ")

# Cadastro do Produto 1
# produto1 = input("Digite o nome do 1o produto: .")
# print(f"Sucesso: {produtol} cadastrado no sistema. \n")
# # Cadastro do Produto 2
# # Cadastro do Produto 3

# # Cadastro do Produto 1
# produto1 = input("Digite o nome do 1o produto: ")
# print(f"Sucesso: (produto1} cadastrado no sistema. \n")

# # Cadastro do Produto 2
# produto2 = input("Digite o nome do 2o produto: ")
# print (f"Sucesso: {produto2} cadastrado no sistema.\n")

# # Cadastro do Produto 3
# produto3 = input("Digite o nome do 3o produto: ")
# print(f"Sucesso: {produto3} cadastrado no sistema. \n")

#segunda_part2
# print(" --- Sistema de Cadastro de Produtos --- ")
# quantidade_produtos = 5 # Imagine que aqui fosse, no futuro, 500 ou 5000
# contador = 1

# # O bloco abaixo será reutilizado diversas vezes
# while contador <= quantidade_produtos:
# produto = input(f"Digite o nome do {contador}º produto: ")
# print(f"Sucesso: {produto} cadastrado no sistema.\n")

# contador = contador + 1 # Prepara para o próximo produto]

#-----------------------------------------------------------------------


# #aula 03 
# # PROJEÇÃO DE RENDIMENTOS (Modelo Iterativo)

# meses_totais = 12
# mes_atual = 1
# saldo_investido = 10000.00
# taxa_juros = 0.01 # Rendimento de 1% ao mês

# print(" --- Relatório de Evolução do Investimento--- ")

# # O fluxo entra no laço iterativo
# while mes_atual <= meses_totais:
# # 1. Calcula o rendimento do mês
# saldo_investido = saldo_investido + ( saldo_investido * taxa_juros)

# #exibe o resultado na tela
# print(f"mês {mes_atual}: o slado atualizado é de r$ {saldo_investido:.2f}")

# # 3. avanço o tempo ( o ´passo crucial p/fluxo retorna)
# mes_atual +=1 

# print("\nprojeção finalizada ")



#-----------------------------------------------------------------------
#aula 04-o controlde de entra
#se no sabermos sonre quando parar o loop e como usarmos, vai procesar a penas uma parte
#temoss q saber usar o loop corretamente 

#Sistema de atualização de tarefas (gestão ágil)

# tarefas_pendentes = 5 

# #1.nossa variavel de controle (o "clicker começando do zero")
# tarefas_concluidas = 0
# print("-- Iniciando a atualização do sistemas --- ")

# #2. nossa condição DE PARADA (continua enquanto houver pendencias)
# while tarefas_concluidas < tarefas_pendentes:
#     #processamento um tarefa 
#     print("Conectando ao banco de dados...")
    
#     #atualizando a variavel de controle (o momento do "click")
#     tarefas_concluidas = tarefas_concluidas +1 
    
#     print(f"Sucesso: tarefa {tarefas_concluidas} movido para 'Finalizada'.\n")
#     # print("--- Todas as tarerfas foram atualizadas. sprint encerrada!---")

#-----------------------------------------------------------------------

#aula 05- Comandos While
# total_servidores = 5
# contador = 1 #nosso pontto de partida

# print("--- Iniciando servidores --- ")
#  # a instrução while (enquanto)
# while contador <= total_servidores:
#     # o bloco de codigo que sera repetido
#     print(f"iniciando o servidor numero{contador}...")
    
#     #a peça mais importante : o incremento !
#     contador = contador + 1  #podemos escrever tb como "contador" +=1
    
#     print("\n Todos os servidores estão online e operacionais")
  
  
# EXEMPLO 2: Comando WHILE com Decremento (Contagem Regressiva)
# import time # Biblioteca simples para simular o tempo real

# tempo_restante = 2 # Nosso ponto de partida agora é o topo

# print("\n --- ALERTA CRÍTICO DE SISTEMA --- ")

# # O laço continua rodando enquanto o tempo for MAIOR que zero
# while tempo_restante > 0:

#  print(f"O sistema será desligado em {tempo_restante} segundos ... ")

# # Simula a espera de 1 segundo do relógio
# time.sleep(2)

# # A peça chave: O Decremento!
# tempo_restante = tempo_restante - 1 # Pode ser escrito como: tempo_restante

# print("SISTEMA DESLIGADO PARA MANUTENÇÃO.")  
    
#-----------------------------------------------------------------------

#aula 06 -     loop Infinito:
#codigo com erro : o pesadelo de loop iinfinito

# import time
# #fila de servidores e serem monitorados
# servidores = ["192.168.1.", "192.168.1.2.", "192.168.1.3"]

# print("iniciando monitoramento... (pressione cltrl + C p/ sair)")

# while servidores:
#     servidor = servidores.pop(0); # pega o 1° servidor da fila 
#     print(f" verificando servidor {servidor}...")
    
#     #simular uma verificação de status 
#     # vamos supor que o servidor e 192.168.1.2 sempre falhe 
    
    
#     if servidor == "192.168.1.2":
#         print(f"Falha de conexão com {servidor}. Reagendando verifição ...")
#         servidor.append(servidor) #reinsere no final da fila 
   
#     else:
#         print(f"servidor {servidor} esta online.") 
        
#     time.sleep(2) #aguardar 2 seg antes da prox. verificação
    
    
#     #2 exemplo
#     import time
#   MAX_TENTATIVAS - 3

# print("Iniciando monitoramento com limite de tentativas ... ")

# while servidores:
#  servidor - servidores.pop(e)
# print(f"Verificando servidor {servidor} ... ")

# if servidor == "192.168.1.2": # Simula falha
#  tentativas[servidor] - tentativas.get(servidor, 0) + 1
# print(f"Falha na conexao com {servidor} (tentativa {tentativas[servidor]})")

# if tentativas[servidor] < MAX_TENTATIVAS:
# print(f"Reagendando {servidor} para nova tentativa ... ")
# servidores. append(servidor)
# else:
# print(f"Numero maximo de tentativas atingido para {servidor}. Descartando.")
# # Não reinsere, apenas registra a falha definitiva

# print(f"Servidor {servidor} esta online.")


#-------------------------------------------
#aula 07- Repetição indeterminada 
#Sistema de gestão de projetos - Menu Interativo

# print(" --- Bem- Vindo ao sistema josue de gestão --- ")

# opcao_escolhida = " "
#  # a condição da parada (repetição indeterminadaa)
#  # le- se: enquanto a opção for diferente de 3, conytinue a rodar.
# while opcao_escolhida != '3':
#     #exibir o men
#     print("\nO que você deseja fazer?")
#     print("1 - Cadastrar nova tarefa")
#     print("2- listrar tarefas da semana")
#     print(" 3 - sair do sistema ")
    
#     # interação com o usuario (o evento exeterno que controla o loop)
#     opcao_escolhida = input("Digite o numero da opção: ")
    
#     # 4. processar a escolha usando a logica condicional que já conhecemos)
#     if opcao_escolhida =="1":
#         print( ">>>Abrindo painel de cadastro de tarefas. .. ")
#     elif opcao_escolhida == "2":
#         print(">>>Buscando tarefas pendentes no banco de dados")
#     elif opcao_escolhida == "3":
#         print(">>> Salvando os .dados e encerrando o sistema. Ate logo!")
#     else:
#         print(">>>Opão inválida! Por favor, digite [1, 2 ou 3].")
        
#         print("sistema encerrada com sucesso ")

#-------------------------------------------------------------------------------------------
#aula 08-
#tabuada - comando for (aulas pratica)
# import time

# for num1 in range(6):
#     print("Tabuada do", num1)
#     for num2 in range(11):
#         print(num1, "x", num2, "=", num1 * num2)
#         time.sleep(2)

#outro exemp.2
#vai comecar de 0, contar ate 157, de 5 em 5.
# for num1 in range(0,157,5):
#     print(" ===> ", num1)

#outro exemp.3
#Geração de credenciais (contador crescente)
# print("--- Sistema de Integração RH|ti --- ")
# #a estrutura for empacota: inicialização, condição e atualização
# #range (inicio, limite_exclusivo, passo)
# for funcionario in range(1,6,1):
#     print(f"Gerando as Credenciais de acesso para o colaborador {funcionario}...")
#     print("--- todas as 5 credenciais foram greradas com sucesso! ---")

#--------------------------------------------------------------------------------------------------------------
#aula 09- comando DO_ while
#incializar uma  variavel 
#exemp.1
# contador = 0
# #executar o corpo do loop (body) pelo menos uma vez 
# while True:
#     print(contador)
#     contador+=1 #incrementa a variavel em 1 
#     if contador >=1058:
        # break #sai do loop (repetição) se o contador for igual ou maior que 5 
    
# while(condição):
 # executa: emula a maneira do_while
 
 #exemp.2
# print("--- sistema de validação de dados ---")

# while True:
#     entrada_usuario= int (input("digite um numero positivo: "))
    
#     if entrada_usuario > 0:
#         print("numero validado com sucesso! ")
#         break 
    
#     print(" entrada invalida. por favor, tente novamente!\n")

#------------------------------------------------------------------------------------
#aula10- controle de fluxo 
#demonstrar o break
# print("\n-- iniciando a varredura de segurança --")
# #simular pacotes de dados. o pacote 4 esta infectado
# #range vai de 1 ao 10 
# for pacote in range (1,11):
#     print(f"analisando pacotes {pacote}...")
    
#     if pacote == 4:
#         print(">> ALERTA CRITICO: virus detectado no pacote 4!")
#         print(">> interrompendo a varredura para proteger o sistema!")
#     break # o break interrompe o loop. nada mais e executado.
#     print(f"Pacote {pacote} seguro.\n")
    
#     print(" --- fim do procesamento de rede ---  ")

#exemp.2
 #demonstrar o continue 
# print("\n -- inicializando financeiro ---")

# for venda in range (1,16):
#  if venda == 7:
#     #simulando que a venda n° 7 foi cancelada 
#   print(f">> venda {venda} foi cancelada, descartando esta venda...")
#  continue # o continue ignora o resto deste bloco e volta para o topo
#  #esta linha Não sera executada para a venda 7 
#  print(f"processando imposto da venda {venda}...")
#  print("--- fechamento finaceiro concluido  --- ")

#------------------------------------------------------------------------------------------
#aula 11-repetição com condição
#sistema e analise financeira de projetos 
# print (" --- inicializando auditoria do extrato ---")
# #uma lista com as transacoes financeiras do mes( em reais)
# extrato = [1500, -300, 2000,-150, -50, 400, 700, -220, -10, -350, -2100, -3000]
# #nossos "totalizadores" (as pastas azul e vermelha nop nosso ex.inicial)
# total_receitas = 0
# total_despesas = 0

# # a repétição: o "for" vai pegar um valor da lista (extrato) por vez
# for transacao in extrato:
#     #2. a condição do "if" avalia o dado atual
#  if transacao > 0:
#     print(f"entrada registrada: R$ {transacao}")
#     total_receitas = total_receitas + transacao #acumulando dinheiro q entrou
#  else:
#      print(f"saida registrada: R$ {transacao}")
#      total_despesas = total_despesas + transacao #acumulando o dinheiro q saiu
     
#      #resultado final (fora da repetição)
#      print("\n --- balanço final do projeto ---")
#      print(f"total de receitas (ganhos): R$ {total_receitas}") 
#      print(f"total de despesas (ganhos): R$ {total_despesas}") 
     
#      saldo_final = total_receitas + total_despesas
#      if saldo_final >= 0:
#          print(f"status: projeto lucrativo (saldo: R$ {saldo_final})")
#      else:
#         print(f"status: projeto em prejuizo (saldo: R$ {saldo_final})")

#--------------------------------------------------------------------------------------------------
#aula 12- repetição encadeada
# print(" --- Gerador de Calendário do Projeto --- ")

# #laço externo (as "fileiras do nosso cinema"
# for sprint in range(1,4): # vai rodar p/ a sprint 1,2 e 3
#         print(f"\n >> iniciando a SPRINT {sprint}")
        
#         #laço interno (as "poltronas" de cada fileira)
#         # oberve a identificação: esse "for" está DENTRO do "for" de cima !
#         for dia in range(1,6): #vai rodar do dia 1 ao 5 
#                 print(f" --- Planejamento as tarefas do dia {dia}...")
                
#                 print(f" << fechamento da SPRINT  {sprint} concluido.")
#exemp.2
#desenhar um quadrado(5x5)
# tamanho = 5
# print("\n----Desenhando  um quadrado ----")

# #laço externo controla as linhas (altura)
# for linha in range( 1, tamanho + 1):
#         #laço interno controla as colunas (largura)
#        for coluna in range( linha):
#                #end= " " impede que o print pula a linha
#         print("*", end="")
        
#         #apos imprimir tpodas as colunas de uma linha, damos um print vazio
#         # apenas p/ pular para a prox. linha do quadrado!
#         print()

#aula 13- encerramento
#concluindo tilha, e mostranfo funções que vimos em aula      
#aula 04
print ("hello world !")

#aula05 comandos e saidas 
print ("estou apredendo python com o prof josue")

print ("esta e a segunda mensagem do bloco 5")

print ("lista de compras: \nArroz\nFeijão\nPicanha")

print ("produtos: \tPreço")
print("Feijão:\t\tR$10,00")

print ("Ele disse: \"oi !\"  ")

print("""
      olha 
             que 
                 legal !
      """)


#aula06_comentarios

 #este programa da boas vibndas ao usuario 
print ("hello world ") # imprimir mensagem

# ola 
# kauane 
# tudo bem ?

#aula07 variaveis e constante
#criando uma variavel (etiqueta é o nome do personagem)



nome_do_personagem ="batman"

#usando a variavel 
print(f"O heroi do jogo é {nome_do_personagem}")

nome_do_personagem ="huck"
print(f"agora... O heroi do jogo é {nome_do_personagem}")



# para criar uma constante em python, escrevemos o nome todo MAIUSCULOS
NOME_DO_JOGO = "Super Python Adventure"
VERSAO = "1.0"
FPS_BASE = 30

#AULA08
#aula_ concatenação
#nossas caixas de informação (variaveis )
print("Olá + mundo ")


NOME_HEROI = "Dunk"  #constante
item_magico = "Espada de Hanoi"
local = "floresta sombria "

print ("o heroi",NOME_HEROI, "Tem uma", item_magico )  #jeito antigo 

#forma certa: f-string
print(f"o nosso heroi se chama {NOME_HEROI}. Ele carrega o objeto chamado {item_magico} pela {local}")

print(f"nome:  {NOME_HEROI}.\nItem carregado: {item_magico} \nLocal: {local}")



#aula09
#aula de comanda de entrada

#perguntar o nome do heroi e guarda na variavel 
nome_do_heroi = input("por favor, digite o nome do heroi da historia: ")

#mostrando o funcionamento : que realmente oque foi digitado, sera guardado
print(f"\nOlá {nome_do_heroi}! que bom ter você conosco nesta historia.")

#aula10- tipos numericos e conversão

idade= input("Digite sua idade: ")    #usuario digita 21

#inteiro (int) são numeros sem virgula [5, 10, -1]
#reais (float) são numeros com casas decimais [1.5, 3.14, 9.99]

idade= 21
altura= 1.55
print(idade + altura)



# # casting ou coversão 
# #forma 1 = recebe texto,  depois converte

idade = int (input("Digite sua idade: "))


#forma 2 (a mais usada ) -  a mais usada, coverte direiro na mesma linha do input 
altura = float (input("Digite sua altura:  (ex:1.55):"))


print(f"Voce tem {idade} anos e mede {altura} metros ")

#aula11- formatar mensagens 
preço =  99.50
print(f"O preço e R$ {preço:.2f}")

#cabeçalho


#aula12-calcular

#adicao 
laranja = 10 
pessoas = 2

total = laranja + 5 
print(f"soma:  {total}")

#divisão 
divisão = 7 / 2 
print(f"7 dividido por 2 é:  {divisão}")


#divisão inteira 
divisão_inteira = 7 /2
print(f"Laranja inteiras por pessoa:  {divisão_inteira}")

#resto de divisão 
sobra = 7 % 2 
print(f"sobraram:  {sobra} laranjas ")

contador = 10 
print(f"antes:  {contador}")
 
# contador+=1 # isso significa o mesmo que contador +1
 #contador = contador + 1

print(f"depois de somar 1:  {contador}")
contador-=5 #tira 5
contador = contador - 5 
print(f"depois de tirar 5:  {contador}")


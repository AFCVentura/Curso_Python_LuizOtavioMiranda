"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_str = input("Digite um número inteiro: ")
try:
    num_int = int(num_str)
    if num_int % 2 == 0:
        print(f"O número {num_int} é PAR")
    else:
        print(f"O número {num_int} é ÍMPAR")
except:
    print("O valor digitado não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite em que hora estamos: ")

try:
    hora = int(hora)
    if hora > 23 or hora <0:
        print("Erro, digite uma hora valida")
    elif hora > 17:
        print("Boa Noite")
    elif hora > 11: 
        print("Boa Tarde")
    elif hora >= 0:
        print("Bom Dia")
    else:
        print("Digite um valor válido para a hora")
except:
    print("Digite um valor válido para a hora (números inteiros de 0 a 23)")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
import sys
nome = input("Digite seu nome: ")

for i in range (0,10):
    i = str(i)
    if i in nome:
        print("Digite um nome sem números")
        sys.exit()
    else:
        i = int(i)
if " " in nome:
    print("Digite um nome sem espaços")
elif nome.isalpha():
    if len(nome) <= 1:
        print("Digite pelo menos duas letras")
    elif len(nome) <= 4:
        print("Seu nome é CURTO")
    elif len(nome) <= 6:
        print("Seu nome é MÉDIO")
    elif len(nome) > 6:
        print("Seu nome é GRANDE")
else:
    print("Digite um nome válido")

# esse aqui eu tentei fazer do jeito mais complicado possível pra tirar todos os erros, certeza que tem um jeito mais fácil mas eu ainda não conheço algum módulo, função ou classe ou sla que faça mais fácil
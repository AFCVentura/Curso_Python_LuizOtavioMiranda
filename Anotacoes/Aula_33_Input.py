'''AULA 33 - INPUT'''

# input() é uma função que permite perguntar dados ao usuário
# Tomar cuidado com o terminal que está sendo usado, pois o terminal de output é read only
# A resposta do usuário no input, caso seja salva numa variável, vai ser salva em tipo str
nome = input("Digite seu nome: ")
print(f"Seu nome é {nome}")
print(f"{nome=}") # Se usar o =  ele imprime o nome da variável = ao valor, é util, dentre outras coisas, pra só testar os valores de uma variável sem ficar escrevendo mais coisas

# Evitar fazer typecasting na mesma linha do input por questões como essa:
numero1=int(input("Digite um número: "))   # Se o dev usar o typecasting 'int' na mesma linha e o usuário digitar algo inválido, como uma letra pro exemplo, o programa já gera erro ali mesmo
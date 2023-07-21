'''AULA 40 - OPERADOR LÓGICO 'AND' '''

# Todas as operações devem ser verdadeiras
# Se a primeira condição for falsa ele nem checa as restantes e mostra a ultima analizada (Avaliação de Curto Circuito)
print(True and False and True)

# Qualquer coisa com valor, mesmo que não tenha nenhuma comparação que te induza a pensar que é um boolean, vai ser um boolean true, com excessão dos valores Falsy e do None:

# Valores Falsy 
# 0, 0.0 e '' em bool:
print(bool(0), bool(0.0), bool(''))
print(True and 0 and False and True)

# Boolean False
print(False)

# Valor None
print(True and None and True) # É um valor que indica um não-valor (???)


'''AULA 41 - OPERADOR LÓGICO 'OR' '''

# Qualquer condição truthy vai tornar a expressão inteira verdadeira
# Caso haja muitas expressões diferentes no if ou while, pode-se usar parenteses pra envolver duas ou mais expressões como se fossem blocos
# A Avaliação de Curto Circuito opera aqui também, se o primeiro valor for verdadeiro ele nem checa o restante e pega o valor do que ele avaliou por último:
print(0 or False or 0.0 or 'abc' or True)
print(type(0 or False or 0.0 or 'abc' or True)) # Ele pega o valor da primeira verdadeira, nesse caso foi uma str 'abc'

# Exemplo interessante: 
senha=input("Senha: ") or "Sem senha"
print(f"Senha: {senha}") # Se o input da senha for pulado, é uma string vazia: '' e portanto é falsy, então ele vai pro or "Sem senha" que é uma string com valor, ou seja, truthy. Gostei bastante desse exemplo do professor


'''AULA 42 - OPERADOR LÓGICO 'NOT' '''

# Inverte expressões: False vira True e vice-versa 

# Exemplo interessante:
senha=input("Senha: ")
if not senha:
    print("Você não digitou nada ") # Não digitar nada faz com que a senha seja Falsy, mas inverter usando o not faz com que ela vire truthy e o if leia ela, mostrando aquilo na tela


'''AULA 43 - OPERADORES LÓGICOS 'IN' E 'NOT IN' '''

# Checa se um determinado caractere está dentro de algo (strings, por exemplo) ou não, mas antes: 
# Strings são Iteráveis, isto é: podem ser analizadas item por item, uma das formas é através do índice, que é a posição de cada 'item' (caractere basicamente) na string
# Imagine uma string chamada "Hello World", existem duas formas de iterar ela:
# H  e  l  l  o     W  o  r  l  d
# 0  1  2  3  4  5  6  7  8  9  10        <- Começando da esquerda (começo) com o número 0 e crescendo
#-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1         <- Começando da direita (final) com o número -1 e diminuindo

hello='Hello World' # Imagine que eu queira acessar o caractere 'o' de 'Hello'
print(hello[4]) # Uso colchetes e o índice positivo do caractere
print(hello[-7]) # Ou uso o índice negativo do caractere

# Exemplo de in e not in:
print('H' in hello) # True
print('G' in hello) # False

if 'ello' in hello: # Pode usar mais de um caractere
    print("HELLO DEV")
elif 'ello' not in hello:
    print("...") # Poderia só usar um else aqui mas fiz assim pra mostrar mesmo

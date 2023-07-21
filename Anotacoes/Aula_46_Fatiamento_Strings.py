''' AULA 46 - Fatiamento de Strings '''



# Strings são iteráveis, ou seja, dá pra manipular e tratar cada elemento dela individualmente
# índice:  0. 1. 2. 3. 4. 5. 6. 7. 8. 9   POSITIVO, Esquerda para Direita. Começa do 0
# string:" a. b. a. c. a. t. e. i. r. o"
# índice:-10.-9.-8.-7.-6.-5.-4.-3.-2.-1  NEGATIVO, Direita para Esquerda. Começa do -1
variavel = "Mengão Esmaga"
print(variavel[0])  #Printa o caractere no índice mostrado
print(variavel[1])
print(variavel[2])

print()
# Agora vamos ao fatiamento
# [inicio:fim:passo]
print(variavel[0:5])  # O ÍNDICE FINAL NÃO ENTRA, TAL QUAL NO FOR
print(variavel[7:12])

print()
# Forma 'correta'
print(variavel[0:6])  # índice final que você quer que aparece +1
print(variavel[7:13])

print()
# Se você colocar o ':' mas não colocar final, o fatiamento vai até o final da string, exemplo:
print(variavel[7:])
# Se fizer isso, porém com índice negativo, ele começa exatamente do índice que você colocou, incluindo ele
print(variavel[-6:])

# Se você colocar o ':' mas não colocar o COMEÇO, o fatiamento começa no começo da string e vai até o final.
print(variavel[:6])
# Fazendo isso, porém com índice negativo, ele ainda assim vai do começo da string, mas para um caractere antes, ou seja, é quase a mesma coisa.
print(variavel[:-7])


# FUNÇÃO len()  <- Exibe a quantidade de caracteres de determinada string ou fatiamento (NÃO EXIBE ÍNDICE, CONTAGEM COMEÇA NO 1, ÍNDICE NO 0)
print(len(variavel))   # Exibe a quantidade de caracteres da string "Mengão Esmaga"
print(len(variavel[1])) # Exibe a quantidade de caracteres do índice 1, que obviamente é só 1
print(len(variavel[0:6])) # Exibe a quantidade de caracteres do fatiamento (dá 6 porque vai de 0 até 5, já que o último não entra)


# Um print compõe nada mais que um fatiamento da seguinte forma:
print(variavel[0:len(variavel):1]) # Começa no índice 0 (começo), vai até a contagem final (que não entra, mas como é um número a mais, a string termina certinho, e o passo é 1 porque o print padrão obviamente vai ler todos os carateres)

# Quanto ao passo:
# '012345678910111213
# 'Mengão Esmaga'
print(variavel[0::3]) # ele vai contar até o número do passo (nesse caso, 3) e vai pegar o caractere, portanto não são 3 espaços vazios entre os caracteres pegos e sim 2.

# Se usar índice negativo, o passo tem que ser negativo também
print(variavel[9:0:-1]) # é indice positivo, mas diminuindo (é que nem no 'for')
print(variavel[-1:-10:-1]) # só funciona se for tudo negativo
print(variavel[-10:-1:1]) # nesse caso, tem que ser positivo, porque tá aumentando o valor, mas a string não vai inverter
print(variavel[::-1]) # Não colocando nada, a string é invertida
# Em resumo, passo positivo lê os valores da esquerda para a direita ->, passo negativo da direita para esquerda <-, caso coloque ao contrário, ele vai imprimir uma linha vazia

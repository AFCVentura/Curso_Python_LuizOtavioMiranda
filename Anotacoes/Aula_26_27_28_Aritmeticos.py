''' AULA 26 - OPERADORADES ARITMÉTICOS'''

# Adição +   <- Dois ints, retorna um int, dois floats retorna um float e misto entre int e float retorna float
# Subtração -   <- Dois ints, retorna um int, dois floats retorna um float e misto entre int e float retorna float
# Multiplicação *  <- Dois ints, retorna um int, dois floats retorna um float e misto entre int e float retorna float
print(10+10)
print(10+10.0)
print(10.0+10.0)
print()
# Divisão /   <- Retorna sempre um float, mesmo que seja .0
print(10/3)
print()
# Divisão Inteira //   <- TRUNCA o número, expressão correta, não é arredondar, é remover os decimais e trocar por 0, caso seja dois inteiros retorna int e o restante float
print(10//3)
print()
# Potenciação **   <- Dois ints, retorna um int, dois floats retorna um float e misto entre int e float retorna float
# Módulo %   <- Resto da divisão - Dois ints, retorna um int, dois floats retorna um float e misto entre int e float retorna float


''' AULA 27 - OUTRAS APLICAÇÕES DO + E DO *'''
# +: Concatenação: Juntar strings, listas ou arrays (vetores e matrizes), termo correto é concatenar. Exemplo:
print('10' + '10')
# Concatenar com + só serve para str com str, como visto antes, str com int ou float gera bug, pra isso, concatene usando ',', f-string ou outro placeholder

# *: Repetição: Repete uma string num determinado número de vezes. Exemplo:
print("oi " * 10)
# Só vale para string com inteiro nesse caso, se usar float no inteiro, ele buga (Até um float .0), se usar string com string também buga, se usar float ou int no lugar da string, ele vai multiplicar

'''AULA 28 - PRECEDÊNCIA'''
# 1º ()
# 2º **
# 3º *, /, //, %
# 4º +, -
# Primeiro dentro dos parênteses, depois fora, caso tenha parenteses dentro de parenteses, ex: (10+(10-5)), resolve os parênteses de dentro pra fora. Caso tenha os outros operadores dentro do parênteses também, eles são resolvidos na mesma ordem que seria fora dele, se tiver operadores de mesma precedência juntos, resolve da esquerda pra direita


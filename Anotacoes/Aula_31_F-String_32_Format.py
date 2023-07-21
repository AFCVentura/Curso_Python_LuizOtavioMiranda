''' AULA 31 - F-STRINGS
 Essas duas aulas também mesclam com conteúdos que estudei por fora sobre PlaceHolders '''
# f-string: colocar a letra f antes da string permite que use chaves pra simplificar a formatação delas usando variáveis ou valores, é chamado de formatted string literal

#{:.2f}: representa um número em formato de ponto flutuante com duas casas decimais.
from math import pi
print(f"Número de pi: {pi:.2f}") # O número de pi é infito mas a formatação pegou os 2 primeiros números, é como uma truncagem
# Esse placeholder também pode ter uma vírgula (:,.2f) pra dividir as casas de centenas e milhares como a gente usa (Na verdade usamos . mas nos EUA é a virgula):
print(f"Eu tenho {100000.12535:,.2f} na conta") # Esse placeholder faz com que ele exiba , pra visualizar melhor o milhar e trunca o valor pra duas casas decimais

# Formatação de Posição (APROFUNDADO NA AULA 45):
#{: <10}: alinha a string à esquerda em um espaço de 10 caracteres.
print(f"Dia: {29:<10}")
#{: ^10}: centraliza a string em um espaço de 10 caracteres.
print(f"Dia: {
      29:^10}")
#{: >10}: alinha a string à direita em um espaço de 10 caracteres.
print(f"Dia: {29:>10}")

''' AULA 32 .FORMAT'''
#.format() 
#{0}: representa o primeiro argumento a ser passado para o método format() ou f-string.
print("Números primos: {0}".format(2,3,5,7,11,13,17)) # Exibe o primeiro argumento
#{1}: representa o segundo argumento a ser passado para o método format() ou f-string, e assim por diante.
print("Números primos: {1}".format(2,3,5,7,11,13,17)) # Exibe o segundo argumento
#{nome_variavel}: se você estiver usando f-strings, pode usar o nome de uma variável diretamente no placeholder, como por exemplo: {nome}.

# Exemplo:
nome="Ventura"
print(f"Nome: {nome}")
a=10.12345
b=20000.12345
c='seloco'
string='a={:.2f}, b={:,.2f}, c={}'.format(a, b, c)
print(string)

# Outros Placeholders
#{...} (Ellipsis): pode ser usado em vez de um grande número de placeholders em uma sequência para indicar que alguns elementos foram omitidos.
print(...) # omitiu esse print
... # Escreve Ellipsis

# %d, %f e %s  (INTERPOLAÇÃO: APROFUNDADO NA AULA 44): funciona como o f-string mas especifico pra int, float e string
idade=18
print("Eu tenho %d anos"% idade) # se usar float ele trunca pra int

altura=1.72
print("Eu meço %f" % altura) # ele formata diferente
print("Eu meço %.2f" % altura) # junta o %f e o :.2f

nomee="Ventura"
print("Eu me chamo %s" % nomee) # Sinceramente prefiro só usar o f-string direto


# Termos:
# Índice: basicamente a ordenação de algo por posição (começa no 0), valores numa lista, parâmetros numa função, etc. função for geralmente utiliza 'for i' porque o i é de index e é a variável de controle

# Argumento: são todas as informações dadas à uma função, classe, método, etc. EX:
print("Hello World") # O Hello World é o argumento
# Esses argumentos podem ser ordenados sem índice:
string='a={:.2f}, b={:,.2f}, c={}'.format(a, b, c) # A primeira chave pega o primeiro argumento do .format(), que é o a, a segunda pega o b e assim vai
# Ou podem ser ordenados com índice
string='a={0:.2f}, b={1:,.2f}, c={2}, c={2}'.format(a, b, c) # Com o índice, eu posso repetir o valor ou mudar de ordem, pois não precisa ser na ordem certinha de 0,1,2,3... que era sem colocar número
#Porém eu ainda posso nomear pra garantir mais confiabilidade ainda:

# Parâmetro Nomeado: Quando o argumento é nomeado:
string='a={0:.2f}, b={1:,.2f}, c={nome3}, c={nome3}'.format(a, b, nome3=c) # Quando eu nomeio um argumento, ele vira um parâmetro nomeado, toda vez que eu fizer isso, eu preciso nomear todos depois dele e não posso mais usar o número do índice pro caso dele, preciso usar o nome

# Método: é uma função dentro de um objeto, algo mais complexo mas esse é o resumo
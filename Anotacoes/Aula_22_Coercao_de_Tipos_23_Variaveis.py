''' AULA 22 - COERÇÃO DE TIPOS '''
# Outros nomes: Conversão, type conversion, typecasting, coercion

# Linguagem de tipagem forte: Uma vez definido o tipo, a linguagem não vai mudar do nada.
# Exemplo: se eu definir uma string '10' e tentar somar com um int 10, ele não vai mudar a string pra int só pra somar, ele vai dizer que não posso fazer essa soma
#print('10'+10)
# Se fosse tipagem fraca, ele poderia mudar a tipagem pra adequar ao que é pedido

# Tipagem estática: Você precisa definir o tipo da variável e ele vai checar (type checking) na hora de compilar (o portugol era assim) geralmente não da pra mudar o tipo depois de colocar pela primeira vez
# Tipagem dinâmica: O tipo da variável é atribuido a partir do valor dela e a checagem rola durante a execução do código.

#Java - tipagem forte e estática
#Python - tipagem forte e dinâmica
#JavaScript - tipagem fraca e dinâmica
#C++ - tipagem forte e estática
#C# - tipagem forte e estática
#PHP - tipagem fraca e dinâmica
#TypeScript - tipagem forte e estática
#Ruby - tipagem forte e dinâmica
#Swift - tipagem forte e estática
#Kotlin - tipagem forte e estática
#Go - tipagem forte e estática
#Rust - tipagem forte e estática
#Scala - tipagem forte e estática
#Lua - tipagem fraca e dinâmica
#Dart - tipagem forte e estática
# TUDO ISSO SEGUNDO O CHATGPT, ELE MESMO DIZ QUE PODEM HAVER OUTRAS VISÕES SOBRE O TEMA

# Converter pra inteiro
print(type(int("10")))

# Converter pra flutuante
print(type(float("10")))

# Converter pra string
print(type(str(10)))

# Converter pra boolean
print(bool(10)) # Vai ser explicado mais pra frente o porquê de algo sem valor ser False e com valor ser True
print(type(bool(10)))
print()


''' AULA 23 - INTRODUÇÃO A VARIÁVEIS '''
# Pascal Case
# Camel Case
# Snake Case
    # Capa Snake
# Kebab Case

# PascalCase: Letras inicias das palavaras maiúsculas, sem espaços entre as palavras:
  # Usada as vezes em classes

# camelCase: Primeira letra de todas minúscula mas as inciais das palavras seguintes são maiúsculas:
  # Usada as vezes em variáveis, funções, métodos e propriedades (ainda nem sei o que são essas coisas)

# snake_case: Tudo minúscula e separa palavras por _: snake_case (eu pessoalmente prefiro)
  # Usada as vezes em variáveis, constantes, funções e campos de bancos de dados

    # CAPA_SNAKE: Tudo maíuscula ao invés de minúscula mas usa _ ainda
      # Não sei se tem algum uso prático

# kebab-case: Tudo minúscula separada por -: kebab-case (Sinceramente me parece a pior, nem da pra declarar variável asssim)
  # Usada em URL's

# = é atribuição
# == é equivalente em valor e tipo NO PYTHON
dez_int=10 # <- atribuí 10 à variavel dez_int
dez_str='10' # <- atribuí '10' à variável dez_str
print(dez_int==dez_str) # <- comparei ambos e deu False pois são "valores iguais" mas de tipos diferentes

# Em outras linguagens como JS por exemplo, == só compara valores, então dez_int==dez_str daria True, pra comparar tipos também, precisaria usar ===, em python já compara valor e tipo com ==
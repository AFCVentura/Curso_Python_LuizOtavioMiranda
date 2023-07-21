'''AULA 44 - INTERPOLAÇÃO DE STRINGS COM %'''

# Já pesquisei sozinho sobre isso antes na aula de f-string e .format() quando quis saber o que eram placeholders, lá encontrei esses %
# Essa é uma forma alternativa ao f-string e o .format de formatar uma string ()
# %s é usado para strings
# %f para floats
# %d ou %i para ints
# %x ou %X para hexadecimais

# Exemplo:
nome=input("Digite seu nome: ")
salario=float(input("Digite seu salário: "))
print("%s, seu salário é de R$%f" %(nome, salario)) # %s para string e %f para float. depois da string, colocamos um % e, entre parênteses, as variáveis que correspondem em ordem ao que eu quero mostrar
# É possivel usar a formatação de decimais que trunca os decimais em excesso igual na f-string dessa forma:
print("%s, seu salário é de R$%.2f" %(nome, salario)) # Repare que eu coloquei o .2 (sem o : antes) entre o % e o f, de forma que fica %.2f ao invés de %f? Isso fará mostrar duas casas decimais apenas

# Agora sobre o hexadecimal: É basicamente um número formado de letras de A até F e números de 0 até 9 (ABCDEF0123456789)
# Os placeholders %x e %X fazem a conversão de algum número INTEIRO para hex com letras em minúsculo e maiúsculo respectivamente:
print("O HEX de %.2f é %x" %(salario,int(salario))) # Como é necessário ser int, converti pra int puramente pra exemplificar
# Embora eu ainda não entenda quase nada sobre Hexadecimais, eles não são comumente mostrados com, por exeplo 1 ou 2 caracateres, portanto caso eu queira mudar isso e acrescentar alguns zeros, posso fazer da seguinte forma:
print("O HEX de %.2f é %08x" %(salario,int(salario))) # Coloco o número 0 entre o % e o x e depois coloco a quantidade de caracteres que quero (não a quantidade de zeros, a quantidade de caracteres no final)

# O ideal é escolher um dos métodos de formatação para usar no dia a dia, de todos os que aprendi 
# (concatenação: '+' ou ','. formatação com f-strings, formatação com .format() e interpolação com %)
# O que me pareceu mais prático e melhor foi a f-string e talvez o .format para algumas situações específicas
# A interpolação me pareceu meio complicada por ter que ficar especificando tipos, o + é péssimo também por correr risco de juntar string e número, a vírgula não é muito prática e o .format() é uma versão melhorada do %
'''AULA 45 - MAIS FORMATAÇÃO COM F-STRINGS'''

# : >10    <- Formatação à esquerda: O número é a quantidade de caracteres que você quer que haja no total, se o valor colocado ter 4 caracteres e você colocar o número 10, ele vai completar com 6 caracteres à esquerda do valor.
print(f"{1510: >10}") 
  # O espaço entre o : e o > pode ser trocado por algum caractere e esse caractere vai ser colocado no lugar
print(f"{1510:+>10}") 

# : <10    <- Formatação à direita: Faz a mesma coisa, mas colocando espaços à direita do valor. Assim como a da esquerda, podemos trocar o 10 por outro número e o espaço em branco por outro caractere
print(f"{1510:+<10}") 

# : ^10    <- Formatação ao centro: Coloca o valor no centro e espalha o restante dos caracteres para completar a quantidade que você colocar ao redor:
print(f"{1510: ^10}")
# Assim como os outros, dá pra trocar o espaço por um caractere:
print(f"{1510:_^10}")

# Toda essa formatação se chama Pad e vai ser MUITO ÚTIL pra eu fazer os cabeçalhos que gosto nos exercícios


# Adicionais ao :.2f
# O primeiro que já foi visto antes é colocar uma , entre o : e o . pra, caso o número seja maior que 1000, mostrar a vírgula pra dividir os milhares, milhões, etc.
print(f"{1000000000:,.0f}") # Bem útil pq tenho uma certa dificuldade de visualizar qual número é sem , ou .

# Mostrar o sinal antes do número usando + ou - entre o : e o .
print(f"{10000000:+.2f}") # Número positivo pedindo positivo
print(f"{-10000000:+.2f}") # Número negativo pedindo positivo
print(f"{-10000000:-.2f}") # Número negativo pedindo negativo
print(f"{10000000:-.2f}") # Número positivo pedindo negativo
# Não dá pra pedir ambos, o ideal é usar o + se quiser mostrar em ambos pois se for negativo já mostra o - e se for positivo vai mostrar o +
# Ou seja, é como se - fosse "Só mostra sinal se for negativo" e + fosse "Mostra sinal pros dois"

# Dá pra tentar juntar esse com o pad:
print(f"{10000000:0>+16.2f}") # Repare na ordem: primeiro o :, depois o caracatere que você quer usar na formatação, depois o sinal (se houver), depois o número de caracteres que você quer no total e depois o .2f

# No caso do pad pra esquerda, pode acontecer do sinal ficar à esquerda do espaçamento e o número à direita
# Caso você queira que o sinal vá junto com o número, você deve usar o = no lugar do > da seguinte forma:
print(f"{10000000:0=+16.2f}") # Trocando o > por =, resolverá esse problema

# Hexadecimal, agora em f-strings
# Em f-strings se faz a conversão da seguinte forma:
print(f'O HEX de 12345 é {12345:x}') # Isso sozinho converte pra hex (x pra min e X pra maius)
print(f'O HEX de 12345 é {12345:08x}') # 0 pra completar e 8 pode trocar pelo tanto que você quiser (HEX geralmente é 4 ou 8)

# Por fim, Conversion Flags: !r, !s e !a: esses caracteres vão no lugar do : e fazem basicamente a mesma coisa mas chamam métodos: !r chama __repr__, !s chama __str__ e !a chama __ascii__, isso é só uma 'curiosidade' pq vai ser explicado só mais pra frente
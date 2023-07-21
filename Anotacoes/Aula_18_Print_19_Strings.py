''' AULA 18 - PRINT'''

# Função sep=""
# Finalidade: mudar o caractere separador das strings
# Exemplo
print("Hello", "World") # Sem sep=""
print("Hello", "World",sep="-") # sep="-" faz com que o espaço no meio vire um -
print("Hello", "World",sep="=+-+=") # sep="=+-+=" faz com que o espaço no meio vire um =+-+=
print()

# Função end=""
# Por padrão essas função é end="\r\n", esse valor corresponde à uma quebra de linha
# Finalidade: editar o que é mostrado depois do último parâmetro da string (Basicamente no final da linha)
# Exemplo:
print("Hello World")
print("Wazap") #Sem edição do end=""
print()

print("Hello World",end="\r\n")
print("Wazap") #Edição redudante
print()

print("Hello World",end="   ")
print("Wazap") #Retira a quebra de linha e troca pelos espaços
print()

print("Hello World",end="\r\n   ")
print("Wazap") #Quebra a linha e coloca os espaços na linha seguinte
print()

print("Hello World \nhello hello")
print("Wazap") #Quebra a linha e coloca o 'hello hello' na linha seguinte
print()

# CRLF e LF - Carriage return + line feed: Usado em sistemas Windows. Line feed: Usado em Linux e Unix. MacOS usa os dois.
# Carriage Return faz com que o cursor volte pro começo da linha, sozinho ele teoricamente faz com que o texto sobrescreva sobre o anterior, mas junto com o Line Feed, ele vai pra linha de baixo, os OS mais modernos têm começado a usar só o LF pra ser suficiente pra pular a linha.
# Windows deveria usar o \r\n (\r do CR e \n do LF) mas aqui no VS Code funciona só o \n porque eles usam a própria biblioteca chamada 'vscode-textbuffer' que lida com essa quebra de linha e torna ela independente do sistema operacional

''' AULA 19 - STRING'''
# Caractere de Escape \
# Finalidade: Permitir o uso de uma aspa dupla dentro de aspas duplas da string e o mesmo com aspas simples dentro de simples
# Exemplo
# print("Olá "Otávio"") Ocorrerá um erro (comentado pra não ficar bugando)
print("Olá \"Otávio\"") # O \ não aparece e permite a existencia de aspas duplas dentro de aspas duplas

# r de expressões regulares (??) que pode ser usado
# Finalidade: permitir que o \ (caractere de escape) também apareça no print
# Exemplo
print(r"Olá \"Otávio\"") #Aparecerá a aspa dupla dentro da string e também a \

# Esse comando r vai ser usado mais pra frente mas por enquanto é muito melhor e mais simples inverter a aspa externa se você precisar usar aspas duplas ou simples especificamente dentro da string
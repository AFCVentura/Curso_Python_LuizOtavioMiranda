''' AULA 49 - Try e Except '''

# Try e Except servem para detectar erros no código (desconsiderando erros de sintaxse)
# Os termos "levantar uma excessão" ou "estourar uma excessão" significam basicamente "aparecer um erro"
# Alternativa ao if e else. A forma mostrada nessa video aula não é a ideal mas é boa para introduzir
# Boa parte das coisas utilizadas em Python são objetos, portanto, se você chamar uma variável e colocar '.', você pode ver basicamente tudo o que dá pra fazer com ela:
numero_teste = '102030'
print(numero_teste.isdigit()) # Exemplo de método que dá pra usar em variável string, esse mostra se tem só números na string

# Aplicação desse método:
num = input("Digite um número: ")
if num.isdigit():
    print(f"Seu número str é: {num}")           
    num = int(num)              # Caso eu decidisse fazer essa conversão antes do if, ia dar erro, e se não tivesse o else, ia dar
    print(f"Seu número int é: {num}")           
    print(f"O dobro do seu número é: {num * 2}")
else:
    print("Você não digitou um número")

print()
# O if e else não checam erros, eles apenas interpretam a lógica, já o try e except não, quando você tem um erro em linha x do try, ele pula para o except
try:
    print(f"Seu número str é: {num}")           
    num = int(num)              # Caso eu decidisse fazer essa conversão antes do if, ia dar erro, e se não tivesse o else, ia dar
    print(f"Seu número int é: {num}")           
    print(f"O dobro do seu número é: {num * 2}")
except:
    print("Você não digitou um número")
# Esse conceito é chamado de Fail Fast, quando você quer errar o quanto antes possível no código para ir até o except
# Exercício de mostrar qual valor é maior

valor_1=input("Digite o primeiro valor: ")
valor_2=input("Digite o segundo valor: ")

if valor_1>valor_2:
    print(f"O {valor_1=} é maior que o {valor_2=}")
elif valor_1<valor_2:
    print(f"O {valor_2=} é maior que o {valor_1=}")
else:
    print("Não foi possível dizer qual valor é maior")


# ASCII: Caracteres em inglês com 7 bits (128 caracteres)
# Unicode: Caracteres de todas as formas de escrita com 21 bits (1,114,112 caracteres)
# UTF-8: Usado na web pra representar caracteres Unicode em sistemas que só suportariam ASCII. Caracteres ASCII usam 1 bit e o restante 2, 3 ou 4 bits.

# Por isso valores string funcionam, pois ele checa a tabela Unicode e vê qual é maior
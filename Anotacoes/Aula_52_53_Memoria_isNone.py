''' AULA 52 - Identidade do Valor do que Está na Memória '''

# Quando você declara uma variável, você está basicamente dando um valor a um local da memória do pc, no entanto essa aula quer mostrar como o interpretador coleta essa informação na memória, para isso, é possível usar a função id:
int = 1020
str = 'bom dia'
float = 10.21
bool = True
list = [10, 20]

print(id(int))
print(id(str))
print(id(float))
print(id(bool))
print(id(list))

# Em alguns casos que dependem de MUITOS fatores (tamanho do objeto, versão do python, versão do pc, etc.), dois objetos (lê-se variáveis já que não sei nada de POO) diferentes com o 'mesmo valor' terão o mesmo id, tipo v1 = 10 e v2 = 10 e os dois tem o id igual mesmo sendo diferentes
int2 = 1020
print()

print(id(int))
print(id(int2))


''' AULA 53 - Flags is, is not e None '''

# Existem determinadas situações onde você pode querer saber através de um bool se o código passou dentro de um if, no entanto nomear uma variável ali dentro dizendo isso não é a melhor forma, pois pode ser confuso para outros devs, além de que é necessário nomear a variável antes do if, pois caso não passe no if, ela não existe e portanto, ocorrerá um erro

'''condicao = False

if condicao:
    passou_if = True'''

# se colocar um else com o passou_if = False fica ruim também por depender do else

# Portanto uma forma de resolver é usando o 'is None', que serve mais ou menos como um == None, segundo o ChatGPT, o 'is' é usado para comparar identidades, ou seja, locais na memória de duas coisas, já o == é para apenas valores

# O código ficaria assim

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True

print(f"Passou no if? {passou_no_if is not None}")

# Se a condição for True, o código passa no if e a variável passou_no_if vira True, portanto, o termo 'is not True', que é uma condição, será verdade, já que a variável não é mais None, e sim True


# O professor diz que esse negócio parece confuso por não ter uma serventia muito óbvia atualmente no curso mas é algo que vai ser usado, além disso ele comenta sobre ser útil caso queira consultar algo que está em outro módulo
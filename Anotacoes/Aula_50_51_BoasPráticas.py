''' AULAS 50 E 51 - Variáveis, Constantes, Complexidade de Código e Boas Práticas'''

# Primeiro conceito: Constantes.
    # São variáveis que nunca mudam, em outras linguagens esse conceito é levado ao pé da letra por existir esse artifício de nunca mudar, no Python sempre é possível mudar, no entanto existe uma convenção para isso: Se a coisa não deve ser mudada no código, deve ser escrita COM LETRAS MAIÚSCULAS

# Segundo conceito: IF's com muitas condições são ruins.
    # Quanto mais complexo for o funcionamento de seu IF, mais difícil de entender o código

# Terceiro conceito: Contagem de complexidade alta é ruim.
    # Contagem de complexidade nada mais é que um termo prático para descrever o quão afastado da margem seu código está, a distância em sí não é o problema, mas sim o que ela significa: Que seu código está muito complexo. Complexidade na programação quase nunca é boa, portanto, deve-se evitar isso.

# Exemplo prático:
velocidade_carro = 61 # Velocidade do carro
quilometragem_pista_carro = 110 # Local na estrada do carro

RADAR_1 = 60  # Velocidade max do radar 1
QUILOMETRAGEM_RADAR_1 = 110 # Local na estrada do radar
RADAR_1_RANGE = 1 # Distância em que o radar detecta
# Repare que as variáveis do carro são em minúsculo e as do radar em maiúsculo, já que o carro irá variar e o radar não

# Suponha que eu queira saber se o carro em algum momento passou da velocidade do radar ou não:
if velocidade_carro > RADAR_1:
    print("O carro foi mais rápido que o limite do radar 1 ")
# Mas agora preciso saber se o carro foi multado ou não, para isso, o carro deve ter passado no range do radar
'''
if  quilometragem_pista_carro >= (QUILOMETRAGEM_RADAR_1 - RADAR_1_RANGE) and quilometragem_pista_carro <= (QUILOMETRAGEM_RADAR_1 + RADAR_1_RANGE):
'''
# Ficou meio longo demais, para isso podemos usar a barra invertida e quebrar a linha do if:
if  quilometragem_pista_carro >= (QUILOMETRAGEM_RADAR_1 - RADAR_1_RANGE) and \
    quilometragem_pista_carro <= (QUILOMETRAGEM_RADAR_1 + RADAR_1_RANGE):
    print("O carro foi multado no radar 1")

# Nesse caso vai dar problema pois o simples ato de passar pelo radar irá multar o carro, para arrumar isso precisamos da velocidade também:
if  quilometragem_pista_carro >= (QUILOMETRAGEM_RADAR_1 - RADAR_1_RANGE) and \
    quilometragem_pista_carro <= (QUILOMETRAGEM_RADAR_1 + RADAR_1_RANGE) and \
    velocidade_carro > RADAR_1:
    print("O carro foi multado no radar 1")

# O código está funcional, porém muito poluído, a melhor forma de consertar isso é criar variáveis que reduzam o código:
acima_velocidade_radar_1 = velocidade_carro > RADAR_1
dentro_range_radar_1 = quilometragem_pista_carro >= (QUILOMETRAGEM_RADAR_1 - RADAR_1_RANGE) and \
                       quilometragem_pista_carro <= (QUILOMETRAGEM_RADAR_1 + RADAR_1_RANGE)

if  dentro_range_radar_1 and acima_velocidade_radar_1:
    print("O carro foi multado no radar 1")
# Embora a declaração de variável tenha ficado longa, imagine um código que vai precisar usar isso várias vezes, em vários radares por exemplo, esse é um dos exemplos práticos do porquê é bom evitar if's poluidos e cheios de condições

# Uma forma mais eficiente ainda é pegar as duas condições em forma de variável que criamos agora e juntar numa:
multado_radar_1 = dentro_range_radar_1 and acima_velocidade_radar_1
if multado_radar_1:
    print("O carro foi multado no radar 1")

# Todas essas alterações podem acabar deixando o código mais longo mas fazem com que seja cada vez mais entendível, a criação de variáveis que comentei que ficou meio poluida também poderia ser esticada e feita em mais etapas para ser mais simples
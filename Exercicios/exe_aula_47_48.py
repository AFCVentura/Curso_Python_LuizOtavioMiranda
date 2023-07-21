'''Exercício:
Peça ao usuário para digitar seu nome e sua idade.
Se o nome e a idade forem digitados, exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {primeira letra}
    A última letra do seu nome é {última letra}
Se nada for digitado em um dos campos, exiba:
"Desculpe, você deixou campo(s) vazio(s)'''

nome = input("Digite seu nome: ")
idade = (input("Digite sua idade: "))
if not nome or not idade:
    print("Desculpe, você deixou campo(s) vazio(s)")
else:
    idade = int(idade)
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        status = "TEM"
    else:
        status = "NÃO TEM"
    print(f"Seu nome {status} espaços")
    print(f"Seu nome contem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")



'''Eu tinha feito a checagem de caracteres assim mas não precisava
    for i in range(0, len(nome)):
        if nome[i] == " ":
            status = "CONTÉM"
            break
        else:
            status = "NÃO CONTÉM"'''

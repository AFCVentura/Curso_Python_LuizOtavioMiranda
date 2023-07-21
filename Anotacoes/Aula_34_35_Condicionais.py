'''AULA 34 - ESTRUTURAS CONDICIONAIS'''
'''if, elif, else'''

# Estrutura:
entrada = input("Digite 'entrar' ou 'sair': ")
if entrada == 'entrar':   # Primeira opção, sempre usar if, não esquecer de usar : no final
    print("Você entrou no sistema")
elif entrada == 'sair':   # Todas as opções depois da primeira que ainda tenham especificações usam elif que significa else if (senão, se)
    print("Você saiu do sistema")
else:   # Opcionalmente pode-se usar o else que se aplica a todas as outras condições além das que foram especificadas antes, sempre vai no final e só uma vez
    print("Digite um valor válido")


'''AULA 35 - REVIEW ESTRUTURAS CONDICIONAIS'''

# é possivel usar uma ellipsis pra pular um if, elif ou else, mas também dá pra usar o comando pass:
if entrada=="entrar":
    ...
elif entrada=="sair":
    pass

# Se uma das condições do bloco de if for verdadeira, ele pula as seguintes mesmo que haja mais uma verdadeira

# O ideal é sempre indentar o bloco com um tab de quatro espaços pra dentro (se usar quantidades diferentes da erro e o ideal é 4, dá pra configurar no rodapé)
# Cálculo IMC
nome=input("NOME: ")
peso=float(input("PESO (KG): "))
altura=float(input("ALTURA (METROS): "))

imc=peso/(altura**2)
print(f"IMC: {imc:.2f}")
print(f"{nome} tem {peso} KG, mede {altura} metro(s) e tem o IMC de {imc:.2f}")

#
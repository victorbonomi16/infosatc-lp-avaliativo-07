nome=str(input("Informe seu nome: "))
idade=str(input("Informe sua idade: "))

dados=[lambda x: nome, lambda x: idade]
for x in dados:
 print(x(0))

numeroSalvo=[]
Par=0
Impar=0
def linhas():
    print("-"*35)

for x in range(10):
    numero=int(input("Informe um numero: "))
    numeroSalvo.append(numero)
par = filter(lambda valor: valor % 2 == 0, numeroSalvo)

for value in par:
    print("Números Pares "+str (value))
linhas()

impar = filter(lambda valor: valor % 2 != 0, numeroSalvo)
for value in impar:
    print("Números Ímpares "+str(value))
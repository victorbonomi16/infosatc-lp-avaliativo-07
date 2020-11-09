numeroSalvo=[]
for x in range(5): 
    numero=int(input("Informe um numero: "))
    numeroSalvo.append(numero)
func = list(filter(lambda x: x >=10, numeroSalvo))
print(func)
n1 = int(input("Informe o primeiro  número: "))
n2 = int(input("Informe o segundo   número: "))
n3 = int(input("Informe o terceiro  número: "))
n4 = int(input("Informe o quarto    número: "))
n5 = int(input("Informe o quinto    número: "))

number=filter(lambda x: '>10' in x, [n1,n2,n3,n4,n5])
print(list(number))

vf = int(input("Informe um número: "))
function = [
    lambda x: x**2,
    lambda x: x**3,
]
for f in function:
    print(f(vf))
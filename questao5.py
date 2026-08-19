a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

delta = b**2 - 4*a*c

if delta > 0:
    print("Duas raízes reais distintas")
elif delta == 0:
    print("Uma raiz real")
else:
    print("Nenhuma raiz real")

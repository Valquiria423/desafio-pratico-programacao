# Questão 4 - Classificador de Triângulos

a = float(input("Digite o primeiro lado A: "))
b = float(input("Digite o segundo lado B: "))
c = float(input("Digite o terceiro lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os lados não formam um triângulo.")

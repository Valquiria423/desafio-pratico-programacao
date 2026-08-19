# Questão 3 mini calculadora
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

op = input("Escolha (+, -, *, /): ")

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("Operação inválida")

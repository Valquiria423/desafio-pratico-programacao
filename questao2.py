idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 64:
    print("Adulto")
elif idade >= 65:
    print("Idoso")
else:
    print("Idade inválida.")

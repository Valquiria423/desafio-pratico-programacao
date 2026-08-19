temperatura = float(input("Digite a temperatura da água em °C: "))

if temperatura <= 0:
    print("Sólido")
elif temperatura < 100:
    print("Líquido")
else:
    print("Gasoso")

nome = input("Digite o nome do hóspede: ")
diarias = int(input("Digite a quantidade de diárias: "))

valor_diaria = 290

if diarias > 7:
    taxa = 6.50
elif diarias == 7:
    taxa = 12.00
else:
    taxa = 16.50

total = (valor_diaria + taxa) * diarias

print("\n--- CONTA DO HOTEL ---")
print("Nome:", nome)
print(f"Total a pagar: R$ {total:.2f}")

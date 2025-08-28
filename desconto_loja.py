total = float(input("Digite o valor total da compra: "))
cliente = input("Digite o tipo de cliente (Normal, Premium ou Vip): ")

cliente = cliente.lower()

desconto = 0

if cliente == "premium":
    desconto = total * 0.15
    print("Desconto de 15% aplicado")
elif cliente == "vip" and total > 200:
    desconto = total * 0.25
    print("Desconto de 25% aplicado")
elif cliente == "vip" and total < 200:
    desconto = total * 0.10
    print("Desconto de 10% aplicado")
else:
    print("Nenhum desconto aplicado")

print(f"Valor do desconto: {desconto}")
print(f"Valor total com desconto: {total - desconto}")

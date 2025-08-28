real = float(input("Digite um valor (em real): "))
moeda = input("Digite a moeda para conversão (Dolar ou Euro): ")

moeda = moeda.lower()

cota_dolar = 5.42
cota_euro = 6.31

if moeda == "dolar":
    conversao = real / cota_dolar
    print(f"{real} = {conversao:.2f}")
elif moeda == "euro":
    conversao = real / cota_euro
    print(f"{real} = {conversao:.2f}")
else:
    print("Escolha invalida")
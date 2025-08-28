alt = float(input("Digite sua altura em metros (ex: 1.75): "))
peso = float(input("Digite seu peso (em kilos): "))

imc = peso / (alt ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30.0:
    print("Obesidade")
else:
    print("Dados inválidos")
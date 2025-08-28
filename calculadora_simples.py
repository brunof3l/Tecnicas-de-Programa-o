print("=== Calculadora ===")
num1 = int(input("Digite um número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = int(input("Digite outro número: "))


if operacao == "+":
    resultado = num1 + num2 
if operacao == "-":
    resultado = num1 - num2
if operacao == "*":
    resultado = num1 * num2
if operacao == "/":
    resultado = num1 / num2

print(f"{num1} {operacao} {num2} = {resultado}")
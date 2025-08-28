lado1 = float(input("Digite o lado de um triângulo: "))
lado2 = float(input("Digite outro lado: "))
lado3 = float(input("Digite outro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Os comprimentos dos lados devem ser números positivos.")
elif lado1 + lado2 > lado3:
    print("É possivel formar um triângulo")
elif lado1 + lado3 > lado2:
    print("É possivel formar um triângulo")
elif lado2 + lado3 > lado1:
    print("É possivel formar um triângulo")
else:
    print("Não é possivel formar um triângulo")
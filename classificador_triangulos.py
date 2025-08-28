comp1 = float(input("Digite o comprimento do primeiro lado: "))
comp2 = float(input("Digite o comprimento do segundo lado: "))
comp3 = float(input("Digite o comprimento do terceiro lado: "))

if comp1 == comp2 == comp3:
    print("O triângulo é equilátero.")
elif comp1 == comp2 or comp1 == comp3 or comp2 == comp3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
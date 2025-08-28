segredo = 100

while True:

    tentativa = int(input("Tente advinhar a senha (Somente numeros): "))

    if tentativa == segredo: 
        print("Parabens você acertou!")
        break
    elif tentativa < segredo:
        print("Muito baixo")
    else:
        print("Muito alto")

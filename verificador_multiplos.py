num = int(input("Digite um numero: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} é divisivel por 3 e 5")
elif num % 5 == 0:
    print(f"{num} é divisil por 5")
elif num % 3 == 0:
    print(f"{num} é divisivel por 3")
else:
    print(f"{num} não é divisil nem por 3 e nem por 5")
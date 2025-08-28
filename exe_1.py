num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"{num1} é o maior entre os dois")
elif num2 > num1:
    print(f"{num2} é o maior entre os dois")
else: 
    print("Os número são iguais")
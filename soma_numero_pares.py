num_pares = {}
def soma_numero_pares(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            soma += i
            num_pares[i] = soma
    return soma
num = int(input("Digite um número: "))
print(f"A soma dos números pares de 1 até {num} é: {soma_numero_pares(num)}")
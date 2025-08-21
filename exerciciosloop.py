#exercicio 1 
# for i in range(1, 11):
#     print(i)
    
#execicio 2
# num = int(input("Digite um numero: "))
# print(f"Tabuada do {num}:")
# for mult in range(1, 11):
#     print(f"{num} x {mult} = {num*mult}")

#exercicio 3
# cont = 11
# while cont >= 2:
#     cont -= 1
#     print(cont)
# print("Fogo")
        
# exercicio 4
# soma = 0 
# for i in range(5):
#     num = int(input(f"Digite o {i+1} numero: "))
#     soma += num
# print(f"O resultado da soma dos numeros é: {soma}")

#exercicio 5
# contador = 0
# while True:
#     nome = input(f"Digite um nome (Digite fim para encerrar o programa):")
#     if nome == "fim":
#         break
#     contador += 1
# print(f"Quantidade de nomes escritos: {contador}")

#exercicio 6 
# qtd = int(input("Quantas notas deseja inserir? "))
# soma = 0
# for i in range(qtd):
#     notas = float(input(f"Digite sua {i+1} nota: "))
#     soma += notas
# media = soma / qtd
# print(f"A media das suas notas é: {media:.2f}")    

#exercicio 7
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha: ")
#     if senha != "python123":
#         print("Senha incorreta")      
    
# print("Acesso liberado!")
    
#exercicio 8 
# palavra = input("Digite uma palavra: ")

# vogais = "aeiou"
# qtd_vogais = 0
# qtd_consoantes = 0

# for letra in palavra:
#     if letra.isalpha():
#         if letra in vogais:
#             qtd_vogais += 1
#         else:
#             qtd_consoantes += 1
# print(f"Quantidade de vogais: {qtd_vogais}\nQuantidade de consoantes: {qtd_consoantes}")

# exercicio 9
# for num in range(1, 21):
#     if num % 2 == 0:
#         print(f"{num} é Par")
#     else:
#         print(f"{num} é Impar")

# exercicio 10
# saldo = 1000.00

# while True:
#     print("===Santoandre===\n=====Menu======")
#     print("1) Ver Saldo\n2) Sacar\n3) Depositar\n4) Sair")
#     opcao = input("Escolha uma opção: ")
    
#     if opcao == "1":
#         print(f"Seu saldo atual é de: {saldo:.2f}")
#     elif opcao == "2":
#         saque = float(input("Digite o valor que deseja sacar: "))
#         if saque <= saldo:
#             saldo -= saque
#             print(f"Saque realizado com sucesso!\nSaldo atual: {saldo:.2f}")
#         else:
#             print("Saldo insuficiente")
#     elif opcao == "3":
#         deposito = float(input("Digite o valor de deposito: "))
#         saldo += deposito
#         print(f"Deposito realizado com sucesso!\nSaldo atual: {saldo:.2f}")
#     elif opcao == "4":
#         print("Obrigado por utilizar o Santoandre!")
#         break
#     else:
#         print("Opção Invalida! Tente novamente.")
    
        
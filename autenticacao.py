senha = 8452
tentativas_max = 3
tentativas = 0

while tentativas < tentativas_max: 
    tentativa = int(input("Digite a senha: "))

    tentativas += 1

    if tentativa == senha:
        print("Acesso liberado!")
        break
    else:
        print("Senha incorreta, Tente novamente")

if tentativas == tentativas_max and tentativa != senha:
    print("Excesso de tentativas, Conta bloqueada!")
senha = ""
resposta = "Acesso liberado"
while senha != "python123":
    senha = input("Digite a senha: ")
    if resposta != "python123":
        resposta = "Senha incorreta, tente novamente"
    if resposta == "python123":
        resposta = "Acesso liberado"
print(resposta)

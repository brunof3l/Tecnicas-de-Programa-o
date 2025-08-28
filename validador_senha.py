while True:
    senha = input("Digite uma senha: ")


    if (len(senha) >= 8 and any(c.isupper() for c in senha) and any(c.isdigit() for c in senha)):
        print("Senha válida!")
        break
    else:
        print("Senha inválida! A senha deve conter:\nTer no minimo 8 caracteres\nConter pelo menos uma letra maiúscula\nConter pelo menos um número")
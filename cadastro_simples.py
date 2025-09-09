dicionario = {}

def cadastrar():
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    dicionario[nome] = {"idade": idade}
    
def listar_cadastros():
    for nome, dados in dicionario.items():
        print(f"Nome: {nome}")
        print(f"Idade: {dados['idade']}")
        print("--------------------")           

while True:
    print("1 - Cadastrar")
    print("2 - Listar cadastros")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar_cadastros()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")

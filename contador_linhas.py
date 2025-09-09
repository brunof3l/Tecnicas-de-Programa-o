with open('lista_de_compras.txt','r') as arquivo:
    linha = arquivo.readlines()
    qtd = len(linha)

print(f"O arquivo tem {qtd} linhas")
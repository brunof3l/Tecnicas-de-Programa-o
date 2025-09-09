with open("lista_de_compras.txt", "w") as arquivo:
    for i in range(1, 4):  
        item = input(f"Digite o {i}º item da sua lista de compras: ")
        arquivo.write(item + "\n")  

print("Lista de compras salva em 'lista_de_compras.txt'.")
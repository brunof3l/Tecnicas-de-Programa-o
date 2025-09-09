with open('lista_de_compras.txt', 'a') as arquivo:
    for i in range(1, 3):  
        item = input(f"Digite o {i}º item adicional: ")
        arquivo.write(item + "\n")  
print("Dados salvos em lista_de_compras.txt")
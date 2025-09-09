with open("nomes.txt", "w") as arquivo:
    for i in range(1, 5):  
        nomes = input(f"Digite o {i}º nome: ")
        arquivo.write(nomes + "\n")  

print("Salvo em 'nomes.txt'.")

with open('nomes.txt', 'r') as arquivo:
   conteudo = arquivo.read()
print("Lista de nomes:")
print(conteudo.upper())
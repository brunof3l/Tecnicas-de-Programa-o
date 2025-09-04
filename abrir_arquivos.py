with open('texto.txt', 'w') as arquivo:
    arquivo.write("Hello World\n")
    arquivo.write("Hello People\n")
    

with open('texto.txt','r') as arquivo:
    conteudo = arquivo.read()
print("Esse é o conteudo do arquivo")
print(conteudo)
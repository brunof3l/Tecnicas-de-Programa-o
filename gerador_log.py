with open('log.txt', 'w') as arquivo:
    for i in range(1,11):
        arquivo.write(str(i) + "\n")

print("Salvo em log.txt")
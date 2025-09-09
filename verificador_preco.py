def verificar_preco(preco):
    if preco < 0:
        print("Preço inválido")
    elif preco <= 100 :
        print("Esse produto é Barato")
    else:
        print("Esse produto é Caro")

preco = float(input("Digite o preço do produto: "))
verificar_preco(preco)

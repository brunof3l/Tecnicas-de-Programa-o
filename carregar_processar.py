import json

with open('produtos.json', 'r') as arquivo:
    produtos = json.load(arquivo)
       

for produto in produtos:
    print(f"Produto: {produto['nome']} - Preço: {produto['preco']}")
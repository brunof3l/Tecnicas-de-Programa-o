import json

produtos = [

    {'nome': "morango", 'preco': 10, 'quantidade': 100},
    {'nome': "melancia", 'preco': 15, 'quantidade': 100},
    {'nome': "pera", 'preco': 5, 'quantidade': 100}
]

with open('produtos.json', 'w') as arquivo:
    json.dump(produtos, arquivo, indent=4)
print("Dados de usuários salvos em produtos.json")
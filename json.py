import json

user = [
    {'id': 1, 'nome': 'Bruno', 'idade': 27},
    {'id': 2, 'nome': 'Vinicius', 'idade': 26}
]

with open('user.json', 'w') as arquivo:
    json.dump(user, arquivo, indent=4)
print("Dados de usuarios salvos em user.json")

with open('user.json', 'r') as arquivo:
    user_lidos = json.load(arquivo)
    print("Dados lidos:")
    print(user_lidos)
import json

user = [
    {'nome': "bruno", 'idade': 27, 'cidade': "tres lagoas"}
    ]

with open('user.json', 'w') as arquivo:
    json.dump(user, arquivo, indent=4)
print("Dados de usuários salvos em user.json")
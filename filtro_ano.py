import sqlite3

ano_corte = 2019

conexao = sqlite3.connect('carros.db')
cursor = conexao.cursor()

query = 'SELECT * FROM carros WHERE ano >= ?'
cursor.execute(query, (ano_corte,))

carros_corte = cursor.fetchall()

if carros_corte:
    print(f"Carros fabricados a partir de {ano_corte}:")
    for carro in carros_corte:
        print(f"ID: {carro[0]}, Marca: {carro[1]}, Ano: {carro[2]}")
else:
    print(f"Nenhum carro encontrado fabricado a partir de {ano_corte}.")

conexao.close()
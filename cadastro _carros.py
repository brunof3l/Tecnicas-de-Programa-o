import sqlite3

conexao = sqlite3.connect('carros.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS carros (
id INTEGER PRIMARY KEY,
marca TEXT NOT NULL,
ano INTEGER NOT NULL
)
''')

cursor.execute("INSERT INTO carros (marca, ano) VALUES ('Argo', 2021)")
cursor.execute("INSERT INTO carros (marca, ano) VALUES ('Civic Type R', 2025)")


conexao.commit()
conexao.close()

print("Banco de dados criado e dados inseridos com sucesso!")
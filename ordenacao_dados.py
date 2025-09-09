import sqlite3

conexao = sqlite3.connect('biblioteca.db')

cursor = conexao.cursor()
cursor.execute("SELECT * FROM livros ORDER BY autor")

linhas = cursor.fetchall()

for linha in linhas:
    print(linha)

conexao.close()
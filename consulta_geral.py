import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

cursor.execute("SELECT id, titulo, autor FROM livros")
for linha in cursor.fetchall():
    print(linha)

conexao.close()
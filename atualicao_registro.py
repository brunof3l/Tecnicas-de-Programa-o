import sqlite3

conexao = sqlite3.connect('biblioteca.db')

cursor = conexao.cursor()
cursor.execute("UPDATE livros SET titulo = 'Harry Potter e o Calice de Fogo' WHERE id = 1")

print("Registro atualizado com sucesso.")

conexao.commit()
conexao.close()
import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()
cursor.execute("DELETE FROM livros WHERE id = '4'")
conexao.commit()    
conexao.close()
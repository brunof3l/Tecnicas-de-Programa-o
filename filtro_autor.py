import sqlite3

autor_especifico = "J.K. Rowling"

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM livros WHERE autor = ?', (autor_especifico,))

livros_do_autor = cursor.fetchall()

if livros_do_autor:
    print(f"Livros encontrados do autor '{autor_especifico}':")
    for livro in livros_do_autor:
        print(f"  ID: {livro[0]}, Título: {livro[1]}")
else:
    print(f"Nenhum livro encontrado do autor '{autor_especifico}'.")

conexao.close()
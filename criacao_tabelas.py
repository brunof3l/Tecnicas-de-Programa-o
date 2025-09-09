import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
id INTEGER PRIMARY KEY,
titulo TEXT NOT NULL,
autor TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO livros (titulo, autor) VALUES ('Harry Potter e a Pedra Filosofal', 'J.K. Rowling')")
cursor.execute("INSERT INTO livros (titulo, autor) VALUES ('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien')")
cursor.execute("INSERT INTO livros (titulo, autor) VALUES ('O Grande Gatsby', 'F. Scott Fitzgerald')")

conexao.commit()
conexao.close()

print("Banco de dados criado e dados inseridos com sucesso!")
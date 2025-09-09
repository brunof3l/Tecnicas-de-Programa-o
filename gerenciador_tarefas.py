import sqlite3

conexao = sqlite3.connect('tarefas.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    descricao TEXT NOT NULL,
    status TEXT NOT NULL
);
''')

cursor.execute("INSERT INTO tarefas (descricao, status) VALUES ('Trabalho Desenvolvimento Web', 'Concluído')")
cursor.execute("INSERT INTO tarefas (descricao, status) VALUES (?, ?)", ('Trabalho Técnicas de Programação', 'Pendente'))

conexao.commit()
conexao.close()

print("Banco de dados criado e tarefas iniciais inseridas.")
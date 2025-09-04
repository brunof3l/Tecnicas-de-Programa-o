import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos
               
               
               ''')

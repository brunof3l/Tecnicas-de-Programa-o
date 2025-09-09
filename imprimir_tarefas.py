import sqlite3

conexao = sqlite3.connect('tarefas.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM tarefas ORDER BY id')
todas_as_tarefas = cursor.fetchall()

print("--- Lista de Tarefas ---")
for tarefa in todas_as_tarefas:
    print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Status: {tarefa[2]}")

conexao.close()
import sqlite3

id_tarefa_concluir = 2

conexao = sqlite3.connect('tarefas.db')
cursor = conexao.cursor()

cursor.execute('UPDATE tarefas SET status = "Concluído" WHERE id = ?', (id_tarefa_concluir,))
conexao.commit()
conexao.close()

print(f"Tarefa com ID {id_tarefa_concluir} foi marcada como concluída.")
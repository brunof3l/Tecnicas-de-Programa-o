# CRUD para Cadastro de Nomes
# Sistema simples com operações Create, Read, Update e Delete

import json
import os

# Lista para armazenar os nomes
nomes = []

def carregar_dados():
    """Carrega os dados do arquivo JSON"""
    global nomes
    try:
        if os.path.exists("nomes.json"):
            with open("nomes.json", "r") as arquivo:
                nomes = json.load(arquivo)
        else:
            nomes = []
    except:
        nomes = []

def salvar_dados():
    """Salva os dados no arquivo JSON"""
    try:
        with open("nomes.json", "w") as arquivo:
            json.dump(nomes, arquivo)
        return True
    except:
        return False

def criar_nome(nome):
    """CREATE: Adiciona um novo nome"""
    if not nome.strip():
        print("Erro: Nome não pode estar vazio!")
        return False
    
    # Verifica se já existe
    for item in nomes:
        if item["nome"].lower() == nome.lower():
            print(f"Erro: Nome '{nome}' já existe!")
            return False
    
    # Adiciona novo nome
    novo_id = len(nomes) + 1
    nomes.append({"id": novo_id, "nome": nome.strip()})
    
    if salvar_dados():
        print(f"Nome '{nome}' criado com sucesso! (ID: {novo_id})")
        return True
    else:
        print("Erro ao salvar dados!")
        return False

def ler_nomes():
    """READ: Lista todos os nomes"""
    if not nomes:
        print("Nenhum nome cadastrado.")
        return
    
    print("Lista de nomes:")
    for item in nomes:
        print(f"ID: {item['id']} | Nome: {item['nome']}")

def atualizar_nome(id_nome, novo_nome):
    """UPDATE: Atualiza um nome existente"""
    if not novo_nome.strip():
        print("Erro: Nome não pode estar vazio!")
        return False
    
    # Procura o nome pelo ID
    for i, item in enumerate(nomes):
        if item["id"] == id_nome:
            nome_antigo = item["nome"]
            item["nome"] = novo_nome.strip()
            
            if salvar_dados():
                print(f"Nome atualizado: '{nome_antigo}' -> '{novo_nome}'")
                return True
            else:
                print("Erro ao salvar dados!")
                return False
    
    print(f"Erro: Nome com ID {id_nome} não encontrado!")
    return False

def deletar_nome(id_nome):
    """DELETE: Remove um nome"""
    # Procura o nome pelo ID
    for i, item in enumerate(nomes):
        if item["id"] == id_nome:
            nome_removido = item["nome"]
            nomes.pop(i)
            
            # Reorganiza os IDs
            for j, item in enumerate(nomes):
                item["id"] = j + 1
            
            if salvar_dados():
                print(f"Nome '{nome_removido}' removido com sucesso!")
                return True
            else:
                print("Erro ao salvar dados!")
                return False


def menu():
    """Menu principal"""
    carregar_dados()
    
    while True:
        print("\n=== SISTEMA CRUD DE NOMES ===")
        print("1. Criar nome")
        print("2. Listar nomes")
        print("3. Atualizar nome")
        print("4. Deletar nome")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ")
        
        if opcao == "1":
            nome = input("Digite o nome: ")
            criar_nome(nome)
        
        elif opcao == "2":
            ler_nomes()
        
        elif opcao == "3":
            try:
                id_nome = int(input("Digite o ID do nome: "))   
                print(f"esse é o nome que você deseja atualizar: {nomes[id_nome - 1]['nome']}")
                print("S - Sim")
                print("N - Não")
                resposta = input("Digite a resposta: ")
                if resposta.lower() == "s":
                    novo_nome = input("Digite o novo nome: ")
                    atualizar_nome(id_nome, novo_nome)
                else:
                    print("Operação cancelada!")
                    menu()
            except IndexError:
                print("Erro: ID não encontrado!")
                menu()
            except ValueError:
                print("Erro: ID deve ser um número!")
        
        elif opcao == "4":
            try:
                id_nome = int(input("Digite o ID do nome: "))
                print(f"esse é o nome que você deseja deletar: {nomes[id_nome - 1]['nome']}")
                print("S - Sim")
                print("N - Não")
                resposta = input("Digite a resposta: ")
                if resposta.lower() == "s":
                    deletar_nome(id_nome)
                else:
                    print("Operação cancelada!")
                    menu()
                deletar_nome(id_nome)
            except IndexError:
                print("Erro: ID não encontrado!")
                menu()
            except ValueError:
                print("Erro: ID deve ser um número!")
        
        elif opcao == "5":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

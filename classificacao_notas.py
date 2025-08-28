qtd = int(input("Quantas notas deseja inserir? "))

notas = []

for i in range(qtd):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)
   
for nota in notas:
    if nota >= 7:
            print(f"{nota}: Aprovado")
    elif nota >= 5 and nota< 7:
            print(f"{nota}: Recuperação")
    else:
            print(f"{nota}: Reprovado")

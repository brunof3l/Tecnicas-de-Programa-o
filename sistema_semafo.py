print("Escolha a cor do semaforo (vermelho, amarelo, verde)")
cor = input("Digite a cor escolhida: ")

cor1 = "vermelho"
cor2 = "amarelo"
cor3 = "verde"

if cor.lower() == cor1:
    print("Pare!")
elif cor.lower() == cor2:
    print("Atenção!")
elif cor.lower() == cor3:
    print("Acelere!")
else:
    print("Cor inválida.")
print("Escolha umas das cores do semáforo:\nvermelho\namarelo\nverde")
cor = input("Digite a cor desejada: ")

cor1 = "vermelho"
cor2 = "amarelo"
cor3 = "verde"

if cor.lower() == cor1:
    print("Pare")
elif cor.lower() == cor2:
    print("Atenção")
elif cor.lower() == cor3:
    print("Acelerar")
else:
    print("Digite uma cor válida")
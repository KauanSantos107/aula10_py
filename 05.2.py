voto = 0
contador = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0

for i in range(1, 101):
    voto = int(input("Qual número do candidato você deseja votar:  "))
    if voto == 1:
        contador += 1
    elif voto == 2:
        contador2 += 1
    elif voto == 3:
        contador3 += 1
    elif voto == 4:
        contador4 += 1
    elif voto == 5:
        contador5 += 1
    elif voto == 6:
        contador6 += 1
    else:
        print("VOCÊ É PETISTA SEU GAY DE MERDA!!!!!!!!!!!!!")
    
print(f"Candidato 1 teve {contador} votos, Candidato 2 teve {contador2} votos, Candidato 3 teve {contador3} votos e o Candidato 4 teve {contador4} votos.\n A quantidade de votos nulos nessa eleição teve {contador5} votos e de votos em branco {contador6}.")
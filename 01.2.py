maior = None
menor = None

for i in range(1, 16):

    altura = float(input("Qual sua altura: "))

    if i == 1:
        maior = altura
        menor = altura

    if altura > maior:
        maior = altura
    elif altura < menor:
        menor = altura


print(menor)
print(maior)

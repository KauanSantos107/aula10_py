a = None
contador = 0

for i in range(1, 6):
    a = int(input("Valores: "))
    if a < 0:
        contador += 1
        
print(contador)
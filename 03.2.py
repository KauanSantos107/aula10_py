fatorial = int(input("Fatorial de: "))
resultado = 1
saida = ""

for i in range(fatorial, 0, -1): 
    resultado = resultado * i
    
    if fatorial == i:
        saida = f"{fatorial}! = {i} X"
    elif i == 1:
        saida = saida + f" {i} = {resultado}"
    else:
        saida = saida + f" {i} X"
    
print(f"{saida}")

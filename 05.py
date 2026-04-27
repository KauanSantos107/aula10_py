tabu = int(input("Qual tabuada deseja: "))
valorInicial = int(input("Valor inicial: "))
valorFinal = int(input("Valor final: "))

for i in range(valorInicial, (valorFinal + 1)):
    
    r = i * tabu
    print(f"{i} x {tabu} = {r}")
nome = input("Qual é o seu nome: ")
tamanhoNome = 0
for i in nome:
    if i != " ":
        print(i)
        tamanhoNome = tamanhoNome + 1
    
print(tamanhoNome)
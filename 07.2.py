nome = input("Digite seu nome completo: ")
primeiroNome = ""

print("\nNome na vertical:")
for letra in nome:
    
    if letra != " ":
        print(letra)
        primeiroNome = primeiroNome + letra
    else:
        break

print("\nNome na horizontal:")
print(primeiroNome)

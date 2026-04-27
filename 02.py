soma_impares = 0 
lista_impares = []

for numero in range (1, 501, 2):
    lista_impares.append(numero)
    soma_impares += numero



print("--- Números Ímpares de 1 a 500 ---")
print(lista_impares)
print("\n" + "="*30)
print(f"A soma total de todos os números pares é: {soma_impares}")
print("="*30)
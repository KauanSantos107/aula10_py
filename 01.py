soma_pares = 0
lista_pares = []


for numero in range(2, 501, 2):
    lista_pares.append(numero)
    soma_pares += numero

# Apresentando os resultados
print("--- Números Pares de 1 a 500 ---")
print(lista_pares)
print("\n" + "="*30)
print(f"A soma total de todos os números pares é: {soma_pares}")
print("="*30)

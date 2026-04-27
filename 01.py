# Inicializamos a variável que guardará o total da soma
soma_pares = 0
# Criamos uma lista vazia para armazenar os números e apresentá-los depois
lista_pares = []

# O range começa em 2, vai até 501 (para incluir o 500) e pula de 2 em 2
for numero in range(2, 501, 2):
    lista_pares.append(numero)
    soma_pares += numero

# Apresentando os resultados
print("--- Números Pares de 1 a 500 ---")
print(lista_pares)
print("\n" + "="*30)
print(f"A soma total de todos os números pares é: {soma_pares}")
print("="*30)
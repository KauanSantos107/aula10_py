soma = 0
lista = []
for i in range(3, 501, 3):
    lista.append(i)
    soma += i

print("--- Números Multiplos de 3 de 1 a 500 ---")
print(lista)
print("\n" + "="*30)
print(f"A soma total de todos os números pares é: {soma}")
print("="*30)
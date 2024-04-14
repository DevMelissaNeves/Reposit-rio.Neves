#3 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_A = []
vetor_B = []

print("Digite os elementos do vetor A:")
for i in range(10):
    elemento_A = int(input(f"Elemento {i + 1}: "))
    vetor_A.append(elemento_A)


print("\nDigite os elementos do vetor B:")
for i in range(10):
    elemento_B = int(input(f"Elemento {i + 1}: "))
    vetor_B.append(elemento_B)

vetor_intercalado = []
for a, b in zip(vetor_A, vetor_B):
    vetor_intercalado.append(a)
    vetor_intercalado.append(b)

print("\nVetor intercalado:")
print(vetor_intercalado)

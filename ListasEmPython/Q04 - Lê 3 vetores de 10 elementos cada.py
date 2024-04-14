#4 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_A = []
vetor_B = []
vetor_C = []


print("Digite os elementos do vetor A:")
for i in range(10):
    elemento_A = int(input(f"Elemento {i + 1}: "))
    vetor_A.append(elemento_A)

print("\nDigite os elementos do vetor B:")
for i in range(10):
    elemento_B = int(input(f"Elemento {i + 1}: "))
    vetor_B.append(elemento_B)


print("\nDigite os elementos do vetor C:")
for i in range(10):
    elemento_C = int(input(f"Elemento {i + 1}: "))
    vetor_C.append(elemento_C)

vetor_intercalado = []
for a, b, c in zip(vetor_A, vetor_B, vetor_C):
    vetor_intercalado.append(a)
    vetor_intercalado.append(b)
    vetor_intercalado.append(c)


print("\nVetor intercalado:")
print(vetor_intercalado)

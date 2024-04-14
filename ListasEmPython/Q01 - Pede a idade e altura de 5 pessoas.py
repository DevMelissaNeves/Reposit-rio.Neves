#1 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []


for i in range(5):
    print(f"Digite os dados da pessoa {i + 1}:")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))

    idades.append(idade)
    alturas.append(altura)


print("\nDados na ordem inversa:")
for i in range(4, -1, -1):
    print(f"Pessoa {i + 1} - Idade: {idades[i]}, Altura: {alturas[i]} metros")

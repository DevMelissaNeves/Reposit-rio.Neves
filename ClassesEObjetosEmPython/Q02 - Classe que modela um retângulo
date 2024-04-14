#2 - Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        area = self.lado_a * self.lado_b
        return area

    def calcular_perimetro(self):
        perimetro = 2 * (self.lado_a + self.lado_b)
        return perimetro


comprimento_local = float(input("Informe o comprimento do local: "))
largura_local = float(input("Informe a largura do local: "))

meu_retangulo = Retangulo(comprimento_local, largura_local)

area_local = meu_retangulo.calcular_area()
perimetro_local = meu_retangulo.calcular_perimetro()

quantidade_pisos = area_local // 1
quantidade_rodapes = perimetro_local // 1

print("\nResultados:")
print(f"Área do local: {area_local} unidades quadradas")
print(f"Perímetro do local: {perimetro_local} unidades lineares")
print(f"Quantidade de pisos necessários: {quantidade_pisos}")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes}")

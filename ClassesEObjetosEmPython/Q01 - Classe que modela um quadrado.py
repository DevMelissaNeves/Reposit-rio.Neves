#1 - Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        area = self.lado ** 2
        return area


meu_quadrado = Quadrado(5)

print("Lado atual do quadrado:", meu_quadrado.retornar_lado())


meu_quadrado.mudar_lado(7)


print("Novo lado do quadrado:", meu_quadrado.retornar_lado())

area_quadrado = meu_quadrado.calcular_area()
print("Área do quadrado:", area_quadrado)

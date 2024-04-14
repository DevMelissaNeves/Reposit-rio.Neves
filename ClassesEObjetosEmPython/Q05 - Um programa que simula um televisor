#5 - Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisor:
    def __init__(self):
        self.canal_atual = 1
        self.volume = 50

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal_atual = novo_canal
            print(f"Canal alterado para {novo_canal}")
        else:
            print("Canal inválido. Deve ser entre 1 e 100.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo. Não é possível aumentar mais.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo. Não é possível diminuir mais.")

    def mostrar_estado(self):
        print(f"Canal Atual: {self.canal_atual}")
        print(f"Volume: {self.volume}")


televisor = Televisor()

televisor.mostrar_estado()


televisor.mudar_canal(5)


televisor.aumentar_volume()
televisor.aumentar_volume()

televisor.diminuir_volume()

televisor.mostrar_estado()

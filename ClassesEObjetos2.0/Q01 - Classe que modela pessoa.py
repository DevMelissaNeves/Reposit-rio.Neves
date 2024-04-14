#1 - Crie uma classe que modele uma pessoa (a) Atributos: nome, idade e endereço (b) Metodos: mostrar endereço e alterar endereço

class Pessoa:
  def __init__(self, nome, idade, endereco):
    self.nome = nome
    self.idade = idade
    self.endereco = endereco

  def mostrar_endereco(self):
    print(f"Endereço: {self.endereco}")

  def alterar_endereco(self, novo_endereco):
    self.endereco = novo_endereco

pessoa = Pessoa("Melissa", 17, "173 Recife")

pessoa.mostrar_endereco()
pessoa.alterar_endereco("173 Ipsep")
pessoa.mostrar_endereco()

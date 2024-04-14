#4 -4. Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga de operador, os metodos para fazer as operacoes de soma, subtracao e produto entre dois numeros

class NumeroComplexo:
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def __add__(self, other):
    return NumeroComplexo(self.real + other.real, self.imag + other.imag)

  def __sub__(self, other):
    return NumeroComplexo(self.real - other.real, self.imag - other.imag)

  def __mul__(self, other):
    return NumeroComplexo(
      self.real * other.real - self.imag * other.imag,
      self.real * other.imag + self.imag * other.real
    )

  def __str__(self):
    return f"{self.real} + {self.imag}i"

numero1 = NumeroComplexo(2, 3)
numero2 = NumeroComplexo(4, 5)

soma = numero1 + numero2
diferenca = numero1 - numero2
produto = numero1 * numero2

print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Produto: {produto}")

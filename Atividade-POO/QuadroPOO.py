1º) Defina classe.

 Uma classe em Python é como um plano ou modelo que define características e comportamentos para criar objetos.
 É como uma receita que especifica como construir algo. 
 Por exemplo, uma classe Carro pode definir atributos como modelo e cor, e métodos como ligar o motor. 
 Ao criar objetos dessa classe, eles herdam essas características e comportamentos.

2º) Defina método

Um método em Python é uma função associada a uma classe que descreve uma ação que um objeto dessa classe pode executar. 
É como uma habilidade ou comportamento que um objeto pode ter, definido dentro da classe.

3º) Defina função

Uma função em Python é um bloco de código reutilizável que executa uma tarefa específica. 
É como uma receita que diz exatamente o que fazer para realizar essa tarefa específica. 
É um conjunto de instruções reutilizáveis que podem ser chamadas sempre que precisar executar essa tarefa.

4º) Pesquise 1 exemplo de função (+ de 10 linhas)

def calcular_soma(n):
    """
    Esta função calcula a soma dos números de 1 a n.
    """
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma
numero = 5
resultado = calcular_soma(numero)
print("A soma dos números de 1 a", numero, "é:", resultado)


5º) Explique o funcionamento da função

Essa função chamada calcular_soma adiciona todos os números de 1 até um número dado n. 
Ela usa um loop para adicionar cada número à variável soma.
Finalmente, retorna o total da soma. Fora da função, escolhemos um número específico para somar, 5 neste caso, e imprimimos o resultado.

6º) Pesquise um exemplo de criação de classe com mais de 10 linhas.

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            print("O carro está ligando...")
            self.ligado = True
        else:
            print("O carro já está ligado.")

    def verificar_ligado(self):
        if self.ligado:
            print("O carro está ligado.")
        else:
            print("O carro está desligado.")

7º) Explique o funcionamento da classe

Esse código define uma classe chamada `Carro`, que representa um carro e possui atributos como marca, modelo, cor e um estado de ligado/desligado.
A classe também tem métodos para ligar o carro e verificar se ele está ligado. 
Fora da classe, um objeto `meu_carro` é criado e seus métodos são chamados para verificar se está desligado, ligá-lo e verificar novamente se está ligado.

8º) Quais os seus atributos?

Os atributos da classe `Carro` são:

  - `marca`: Representa a marca do carro.
  - `modelo`: Representa o modelo do carro.
  - `cor`: Representa a cor do carro.
  - `ligado`: Representa o estado do carro, indicando se está ligado (True) ou desligado (False).

9º) Quais os seus métodos?

Os métodos da classe `Carro` são:

  - `__init__`: Método especial de inicialização que define os atributos do carro quando um objeto é criado.
  - ` ligar`: Método que simula a ação de ligar o carro, alterando o estado do atributo `ligado` para True.
  - `verificar_ligado`: Método que verifica o estado do carro e imprime uma mensagem indicando se está ligado ou desligado.

10º) Cite e explique os principais tipos de dados

1. **Inteiros (int)**: Números inteiros, como 5, -10, 100.
2. **Números de ponto flutuante (float)**: Números reais, como 3.14, 2.5, -0.001.
3. **Strings (str)**: Sequências de caracteres, como "Olá, mundo!", 'Melissa Neves'.
4. **Booleanos (bool)**: Valores de verdadeiro (`True`) ou falso (`False`).
5. **Listas (list)**: Coleções ordenadas de itens, definidas entre colchetes `[]`.
6. **Tuplas (tuple)**: Coleções ordenadas de itens imutáveis, definidas entre parênteses `()`.
7. **Dicionários (dict)**: Coleções de pares chave-valor, definidas entre chaves `{}`.

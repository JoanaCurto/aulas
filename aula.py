import numpy as np
import matplotlib.pyplot as plt  # Corrigido o nome do módulo importado
def exemploGrafico():
    # Gerar dados para o gráfico
    x = np.linspace(0, 10, 100)
    y = x

    # Criar o gráfico
    plt.plot(x, y, label='y = x')

    # Adicionar título e rótulos aos eixos
    plt.title('Gráfico de y = x')
    plt.xlabel('x')
    plt.ylabel('y')

    # Adicionar uma legenda
    plt.legend()

    # Mostrar o gráfico

    plt.show()

def add(x, y):
    """
    Função que retorna a soma de x e y.
    """
    return x + y

def subtract(x, y):
    """
    Função que retorna a diferença entre x e y.
    """
    return x - y

def multiply(x, y):
    """
    Função que retorna o produto de x e y.
    """
    return x * y

def divide(x, y):
    """
    Função que retorna a divisão de x por y.
    Retorna uma mensagem de erro se y for 0.
    """
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def calculator():
    """
    Função principal que permite ao usuário selecionar uma operação e inserir números para realizar a operação escolhida.
    """
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a escolha (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Escolha inválida!")

if __name__ == "__main__":
    exemploGrafico()
    calculator()
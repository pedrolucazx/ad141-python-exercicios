# Exercicio 5
# Escreva uma aplicacao de calculadora com o menu:
#
# Calculator options:
#       1. Add
#       2. Subtract
#       3. Multiply
#       4. Divide
#       5. Quit
#
# O usuario deve informar um numero do menu.
# Depois de escolher a operacao, o usuario deve informar 2 numeros.
# A operacao escolhida deve ser executada e o resultado exibido.
#
# Cada opcao do menu deve ser implementada em sua propria funcao.


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: divisao por zero"
    return a / b


def sair():
    return "Saindo da calculadora..."


def opcao_invalida(*_):
    return "Opcao invalida."


def ler_inteiro(mensagem):
    data = input(mensagem)
    if data.startswith("-"):
        numero = data[1:]
    else:
        numero = data

    if not numero.isdigit():
        return None

    return int(data)


operacoes = {
    "1": somar,
    "2": subtrair,
    "3": multiplicar,
    "4": dividir,
    "5": sair,
}

while True:
    print("Calculator options:")
    print("      1. Add")
    print("      2. Subtract")
    print("      3. Multiply")
    print("      4. Divide")
    print("      5. Quit")

    opcao = input("Escolha uma opcao: ")

    if opcao == "5":
        print(operacoes[opcao]())
        break

    fn = operacoes.get(opcao, opcao_invalida)
    if fn is opcao_invalida:
        print(fn(), "\n")
        continue

    primeiro = ler_inteiro("Digite o primeiro numero: ")
    segundo = ler_inteiro("Digite o segundo numero: ")

    if primeiro is None or segundo is None:
        print("Entrada invalida. Digite apenas numeros inteiros.\n")
        continue

    print("Resultado:", fn(primeiro, segundo))
    print()

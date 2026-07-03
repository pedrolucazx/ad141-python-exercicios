# Exercicio 2
# Teste o Exercicio 1 usando alguns numeros negativos como indice.
# Elimine numeros negativos como indices legitimos levantando
# a excecao IndexError quando um numero negativo for fornecido.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    value = input("Digite um indice (ou 'end' para sair): ")
    if value == "end":
        break
    try:
        idx = int(value)
        if idx < 0:
            raise IndexError("indice negativo nao permitido")
        print("Valor:", numbers[idx])
    except ValueError:
        print("Erro: valor nao e um numero inteiro")
    except IndexError as e:
        print("Erro de indice:", e)
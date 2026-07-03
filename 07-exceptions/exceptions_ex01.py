# Exercicio 1
# Crie uma lista com 10 numeros.
# Em um loop, peca ao usuario um numero.
# Use este numero como indice na lista e imprima o valor naquele indice.
# Termine o programa quando o usuario digitar "end".
# Trate o caso de numero invalido (ValueError).
# Trate o caso de indice invalido (IndexError).

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    value = input("Digite um indice (ou 'end' para sair): ")
    if value == "end":
        break
    try:
        idx = int(value)
        print("Valor:", numbers[idx])
    except ValueError:
        print("Erro: valor nao e um numero inteiro")
    except IndexError:
        print("Erro: indice fora do intervalo")
# Exercicio 3
# Escreva um programa que usa um loop para solicitar ao usuario
# um valor inteiro. O programa deve imprimir a soma de todos os
# inteiros inseridos.
#
# Se o usuario digitar uma linha em branco ou qualquer linha que
# nao possa ser convertida em inteiro, trate o ValueError.
#
# Se o usuario usar Ctrl+C para encerrar, trate KeyboardInterrupt.
#
# Quando o usuario digitar Ctrl+D, trate EOFError, saia do loop
# e imprima a soma.

total = 0

while True:
    try:
        line = input("Digite um numero inteiro: ")
        try:
            total += int(line)
            print("Soma parcial:", total)
        except ValueError:
            print("Entrada invalida, tente novamente")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuario")
        break
    except EOFError:
        print()
        break

print("Total:", total)
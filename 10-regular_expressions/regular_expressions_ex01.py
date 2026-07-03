# Exercicio 1
# Escreva um programa que leia uma linha por vez e determine
# se a entrada consiste unicamente em um numero inteiro,
# positivo ou negativo. Indique se ele e positivo ou negativo.

import re


def main():
    print("Digite 'quit' para sair")
    while True:
        texto = input("Digite um valor: ")
        if texto == "quit":
            break

        if re.fullmatch(r"[+-]?\d+", texto):
            if texto.startswith("-"):
                print("Negativo")
            else:
                print("Positivo")
        else:
            print("Nao e um inteiro valido")


if __name__ == "__main__":
    main()

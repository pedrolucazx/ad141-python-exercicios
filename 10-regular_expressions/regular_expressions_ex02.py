# Exercicio 2
# Repita o exercicio anterior, mas agora com numero de ponto
# flutuante. Um numero de ponto flutuante deve ter pelo menos
# um digito a esquerda e a direita do ponto decimal.
# Indique se o numero e positivo ou negativo.

import re


def main():
    print("Digite 'quit' para sair")
    while True:
        texto = input("Digite um valor: ")
        if texto == "quit":
            break

        if re.fullmatch(r"[+-]?\d+\.\d+", texto):
            if texto.startswith("-"):
                print("Negativo")
            else:
                print("Positivo")
        else:
            print("Nao e um numero de ponto flutuante valido")


if __name__ == "__main__":
    main()

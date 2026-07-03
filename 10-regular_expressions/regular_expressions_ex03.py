# Exercicio 3
# Escreva um programa que leia linhas do usuario para verificar
# se estao formatadas conforme os criterios abaixo:
#
# Linhas formatadas corretamente devem conter:
#   - Um identificador de 4 caracteres (2 digitos seguidos de 2 letras maiusculas)
#   - Qualquer numero de espacos ou tabs
#   - Uma descricao
#
# Para cada linha formatada corretamente, imprima os 2 digitos,
# os 2 caracteres e a descricao, cada um em uma linha separada.

import re


def main():
    print("Digite linhas para validar ('quit' para sair)")
    print("Formato esperado: XXYY  descricao")
    print("  XX = 2 digitos, YY = 2 letras maiusculas")
    while True:
        texto = input("Linha: ")
        if texto == "quit":
            break

        match = re.fullmatch(r"(\d{2})([A-Z]{2})[ \t]+(.+)", texto)
        if match:
            print("Digitos:", match.group(1))
            print("Caracteres:", match.group(2))
            print("Descricao:", match.group(3))
        else:
            print("Formato invalido")
        print()


if __name__ == "__main__":
    main()

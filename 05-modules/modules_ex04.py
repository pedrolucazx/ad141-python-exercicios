# Exercicio 4
# Escreva um programa que some os argumentos
# recebidos pela linha de comando.
#
# O programa deve imprimir:
# 1) a soma dos argumentos
# 2) a media dos valores

import sys

args = sys.argv[1:]
numeros = [float(arg) for arg in args]
soma = sum(numeros)
media = soma / len(numeros) if numeros else 0

print(f"Soma: {soma}")
print(f"Media: {media}")

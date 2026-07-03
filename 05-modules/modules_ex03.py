# Exercicio 3
# Escreva um programa que ordene os argumentos
# recebidos pela linha de comando.

import sys

args = sys.argv[1:]
args.sort()

for arg in args:
    print(arg)

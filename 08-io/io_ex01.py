# Exercicio 1
# Escreva um programa que conte o numero de linhas, palavras e caracteres
# em cada arquivo informado na linha de comando.

import sys


for filename in sys.argv[1:]:
    lines = words = chars = 0
    with open(filename) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    print(f"{lines:>4} {words:>4} {chars:>4} {filename}")
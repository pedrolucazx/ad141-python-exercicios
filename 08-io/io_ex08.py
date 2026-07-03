# Exercicio 8
# Leia todos os arquivos fornecidos na linha de comando (um nome por linha)
# e imprima quantas vezes cada linha ocorre no total entre todos os arquivos.

import sys

if len(sys.argv) < 2:
    print(f"Uso: {sys.argv[0]} <arquivo1> <arquivo2> ...")
    sys.exit(1)

counts = {}

for filename in sys.argv[1:]:
    with open(filename) as f:
        for line in f:
            name = line.strip()
            if name:
                counts[name] = counts.get(name, 0) + 1

for name in sorted(counts):
    print(f"{name:<12} {counts[name]}")
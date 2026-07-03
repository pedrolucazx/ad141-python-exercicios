# Exercicio 7
# Leia dois arquivos (um nome por linha) e liste apenas os nomes
# que estao em ambos. Os nomes dos arquivos sao fornecidos na linha
# de comando.

import sys

if len(sys.argv) != 3:
    print(f"Uso: {sys.argv[0]} <arquivo1> <arquivo2>")
    sys.exit(1)


def read_names(filename):
    with open(filename) as f:
        return {line.strip() for line in f if line.strip()}


names1 = read_names(sys.argv[1])
names2 = read_names(sys.argv[2])

for name in sorted(names1 & names2):
    print(name)
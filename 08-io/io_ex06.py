# Exercicio 6
# Exiba o nome, tamanho e data de modificacao de todos os arquivos
# em um diretorio que sejam maiores que um determinado tamanho.
# O diretorio e o tamanho minimo sao fornecidos como argumentos
# de linha de comando.

import sys
import os
import time

if len(sys.argv) != 3:
    print(f"Uso: {sys.argv[0]} <diretorio> <tamanho_minimo>")
    sys.exit(1)

directory = sys.argv[1]
min_size = int(sys.argv[2])

for entry in os.listdir(directory):
    path = os.path.join(directory, entry)
    if os.path.isfile(path):
        size = os.path.getsize(path)
        if size > min_size:
            mtime = time.ctime(os.path.getmtime(path))
            print(f"{entry:<30} {size:>10} {mtime}")
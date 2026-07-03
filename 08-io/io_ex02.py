# Exercicio 2
# Revise o Exercicio 1 para aceitar um -t como primeiro argumento opcional.
# Quando -t for fornecido, mostre apenas os totais combinados
# de linhas, palavras e caracteres de todos os arquivos.

import sys


files = sys.argv[1:]
totals_only = False

if files and files[0] == "-t":
    totals_only = True
    files = files[1:]

total_lines = total_words = total_chars = 0

for filename in files:
    lines = words = chars = 0
    with open(filename) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    total_lines += lines
    total_words += words
    total_chars += chars
    if not totals_only:
        print(f"{lines:>4} {words:>4} {chars:>4} {filename}")

if totals_only:
    print(f"{total_lines:>4} {total_words:>4} {total_chars:>4} total")
elif len(files) > 1:
    print(f"{total_lines:>4} {total_words:>4} {total_chars:>4} total")
# Exercicio 4
# Obtenha os nomes dos arquivos da linha de comando se 2 argumentos
# forem fornecidos. Caso contrario, peca ao usuario.

import sys

if len(sys.argv) == 3:
    in_name = sys.argv[1]
    out_name = sys.argv[2]
else:
    in_name = input("Digite o nome do arquivo de entrada: ")
    out_name = input("Digite o nome do arquivo de saida: ")

with open(in_name) as f_in:
    with open(out_name, "w") as f_out:
        while True:
            line = f_in.readline()
            if not line:
                break
            f_out.write(line)

print("Copia concluida.")
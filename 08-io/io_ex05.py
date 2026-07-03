# Exercicio 5
# Adicione tratamento de excecao ao exercicio anterior para que,
# se a abertura de um arquivo falhar, um OSError seja tratado
# e o programa seja encerrado.

import sys


def get_filenames():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    in_name = input("Digite o nome do arquivo de entrada: ")
    out_name = input("Digite o nome do arquivo de saida: ")
    return in_name, out_name


in_name, out_name = get_filenames()

try:
    with open(in_name) as f_in:
        with open(out_name, "w") as f_out:
            while True:
                line = f_in.readline()
                if not line:
                    break
                f_out.write(line)
except OSError as e:
    print("Erro:", e)
    sys.exit(1)

print("Copia concluida.")
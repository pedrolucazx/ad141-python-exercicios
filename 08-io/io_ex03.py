# Exercicio 3
# Peca ao usuario os nomes de um arquivo de entrada e um de saida.
# Leia do arquivo de entrada (usando readline()) e escreva no de saida
# (usando write()).

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
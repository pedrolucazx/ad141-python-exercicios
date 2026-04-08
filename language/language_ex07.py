# Exercicio 7
# Use um `range` para percorrer e imprimir cada numero de 0 a 49,
# produzindo a seguinte saida.
#
# Cada numero deve ser impresso individualmente, em vez de concatenar
# tudo como uma unica string.
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

for number in range(50):
    print(f"{number:2}", end=" ")
    if (number + 1) % 10 == 0:
        print()

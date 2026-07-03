# Exercicio 1
# Defina algumas funcoes e coloque-as em um modulo.
#
# Em seguida, escreva um programa Python em um arquivo separado
# que importe o modulo e chame as funcoes.

import math_funcs


def test():
    print("square(4):", math_funcs.square(4))
    print("cube(3):", math_funcs.cube(3))


test()

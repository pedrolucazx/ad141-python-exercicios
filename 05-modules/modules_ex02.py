# Exercicio 2
# Crie um novo arquivo e defina nele uma funcao com o mesmo nome
# (mas com comportamento diferente) de uma das funcoes do exercicio anterior.
#
# Em um arquivo separado, crie uma aplicacao que importe:
# 1) o modulo deste exercicio
# 2) o modulo do exercicio anterior
#
# A aplicacao deve conseguir chamar com sucesso
# todas as funcoes dos dois modulos importados.

import math_funcs
import alt_math


def test():
    print("math_funcs.square(4):", math_funcs.square(4))
    print("alt_math.square(4):", alt_math.square(4))
    print("math_funcs.cube(3):", math_funcs.cube(3))
    print("alt_math.cube(3):", alt_math.cube(3))


test()

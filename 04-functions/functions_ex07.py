# Exercicio 7
# Escreva e teste uma funcao que recebe:
# - uma quantidade variavel de argumentos como primeiro parametro
# - um numero como segundo parametro (num)
#
# A funcao deve retornar a quantidade de valores, dentro da tupla
# de argumentos variaveis, que sao maiores do que o segundo parametro.
#
# Exemplo:
# res = positive(5, -10, 10, -20, 30, num=0)
# Nesse caso, o retorno deve ser 3.


def positive(*valores, num):
    quantidade = 0
    for valor in valores:
        if valor > num:
            quantidade += 1
    return quantidade


res = positive(5, -10, 10, -20, 30, num=0)
print(res)

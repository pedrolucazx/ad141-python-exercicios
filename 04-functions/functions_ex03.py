# Exercicio 3
# Existe uma funcao nativa em Python chamada sum,
# que soma todos os numeros de um iteravel.
#
# Escreva uma funcao semelhante, mas em vez de receber
# uma colecao como parametro, a funcao deve receber
# uma quantidade variavel de argumentos e retornar a soma deles.


def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(10, 20, 30, 40))

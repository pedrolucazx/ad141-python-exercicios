# Exercicio 6
# Escreva e teste uma funcao que recebe uma lista
# como unico parametro e retorna uma nova lista
# contendo apenas os elementos positivos.


def apenas_positivos(lista):
    positivos = []
    for numero in lista:
        if numero > 0:
            positivos.append(numero)
    return positivos


valores = [10, -4, 25, 0, -1, 8]
print(apenas_positivos(valores))

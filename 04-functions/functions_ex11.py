# Exercicio 11
# Escreva e teste uma funcao que recebe duas listas
# como parametros e retorna uma lista com os elementos
# que sao comuns a ambas.


def elementos_comuns(lista1, lista2):
    return list(set(lista1) & set(lista2))


primeira = [1, 2, 3, 4, 5, 2]
segunda = [2, 4, 6, 8, 2]
print(elementos_comuns(primeira, segunda))

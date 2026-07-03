# Exercicio 4
# Reescreva a funcao do Exercicio 3 para retornar
# uma tupla em vez de um unico valor.
#
# A tupla deve conter:
# 1) a soma de todos os argumentos
# 2) a media de todos os argumentos


def soma_e_media(*numeros):
    total = 0
    for numero in numeros:
        total += numero

    media = total / len(numeros)
    return total, media


resultado = soma_e_media(5, 10, 15, 20)
print(resultado)

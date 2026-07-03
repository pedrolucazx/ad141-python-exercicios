# Exercicio 12
# Escreva e teste uma funcao que recebe:
# - um numero
# - um dicionario
#
# A funcao deve somar o numero a todos os valores do dicionario.
# Considere que todos os valores do dicionario sao numericos.


def somar_em_todos(valor, dados):
    novo_dicionario = {}
    for chave in dados:
        novo_dicionario[chave] = dados[chave] + valor
    return novo_dicionario


info = {"a": 10, "b": 20, "c": 30}
print(somar_em_todos(5, info))

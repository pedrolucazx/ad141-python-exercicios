# Exercicio 10
# Reescreva a solucao do Exercicio 8 ou 9
# para usar uma expressao lambda
# como funcao aninhada.


def criar_soma_lambda():
    soma = lambda a, b: a + b
    return soma


funcao_soma = criar_soma_lambda()
print(funcao_soma(20, 35))

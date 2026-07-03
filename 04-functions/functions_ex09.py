# Exercicio 9
# Reescreva a solucao do Exercicio 8 para que
# a funcao externa nao receba parametros.
#
# A funcao aninhada deve ser definida para receber
# os dois parametros.


def criar_soma():
    def somar(a, b):
        return a + b

    return somar


funcao_soma = criar_soma()
print(funcao_soma(7, 3))

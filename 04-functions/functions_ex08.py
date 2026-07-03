# Exercicio 8
# Escreva uma funcao que retorna uma funcao aninhada.
#
# Quando a funcao aninhada for executada,
# ela deve retornar a soma de dois inteiros.
#
# Os dois parametros devem ser passados para a funcao externa
# e utilizados pela funcao interna.


def criar_soma(a, b):
    def somar():
        return a + b

    return somar


funcao_soma = criar_soma(12, 8)
print(funcao_soma())

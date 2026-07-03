# Exercicio 2
# Escreva e teste uma funcao que recebe uma colecao de strings
# e retorna o tamanho da maior string da colecao.
#
# A aplicacao deve percorrer a colecao e usar o valor retornado
# pela funcao para formatar a saida.
#
# Todas as strings devem ser impressas alinhadas a direita
# com a largura da maior string.


def tamanho_maior_string(colecao):
    maior = 0
    for texto in colecao:
        if len(texto) > maior:
            maior = len(texto)
    return maior


frases = [
    "Banana",
    "Manga",
    "Abacaxi",
    "Pera",
    "Melancia",
]

largura = tamanho_maior_string(frases)
for item in frases:
    print(f"{item:>{largura}}")

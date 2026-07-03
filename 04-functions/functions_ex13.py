# Exercicio 13
# O metodo index de list permite localizar a primeira ocorrencia
# de um item (ou a primeira dentro de um intervalo),
# mas nao permite informar diretamente qual ocorrencia exata
# (segunda, terceira, etc.) voce quer encontrar.
#
# Escreva uma funcao com 3 parametros:
# 1) a lista a ser pesquisada
# 2) o objeto a ser procurado
# 3) um int representando qual ocorrencia buscar
#    (primeira, segunda, terceira, etc.)
#
# O metodo index levanta ValueError quando o valor nao existe na lista.
# E aceitavel que sua funcao tenha o mesmo comportamento.


def indice_da_ocorrencia(lista, valor, ocorrencia):
    indice = -1
    for _ in range(ocorrencia):
        indice = lista.index(valor, indice + 1)
    return indice


dados = [10, 20, 10, 30, 10, 40]
resultado = indice_da_ocorrencia(dados, 10, 2)

if resultado == -1:
    print("Valor ou ocorrencia nao encontrados")
else:
    print(resultado)

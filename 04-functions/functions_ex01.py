# Exercicio 1
# Escreva e teste uma funcao para validar entrada.
#
# A funcao deve solicitar ao usuario um numero inteiro positivo.
# Valide se o valor informado e, de fato, um inteiro positivo.
#
# Se o valor for valido, a funcao deve retornar o numero.
# Se o valor for invalido, a funcao deve retornar 0.
#
# A aplicacao (e nao a funcao) deve exibir uma mensagem de erro
# sempre que uma entrada invalida for informada.


def validar_numero_positivo():
    data = input("Digite um numero inteiro positivo: ")
    if not data.isdigit():
        return 0

    numero = int(data)
    if numero <= 0:
        return 0

    return numero


while True:
    resultado = validar_numero_positivo()
    if resultado == 0:
        print("Entrada invalida. Tente novamente.")
    else:
        print(f"Numero valido: {resultado}")
        break

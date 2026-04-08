# Exercicio 6
# Peca ao usuario tres numeros que representem:
# - um limite inferior
# - um limite superior
# - um valor de passo
#
# O programa deve usar um objeto `range` para percorrer e imprimir
# os numeros do menor para o maior, incluindo o limite superior,
# levando em consideracao o passo informado.

lower_limit = int(input("Digite o limite inferior: "))
upper_limit = int(input("Digite o limite superior: "))
step_value = int(input("Digite o valor de passo: "))

for number in range(lower_limit, upper_limit + 1, step_value):
    print(number)

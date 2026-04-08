# Exercicio 8
# Reescreva o exercicio 4 para considerar tambem o caso em que
# o primeiro numero informado seja maior que o segundo.
#
# Exemplo 1:
# Se o usuario informar 10 e 15, a soma deve ser 75.
# 10 + 11 + 12 + 13 + 14 + 15 = 75
#
# Exemplo 2:
# Se o usuario informar 15 e 10, a soma ainda deve ser 75.

first_number = int(input("Digite o primeiro numero inteiro: "))
second_number = int(input("Digite o segundo numero inteiro: "))

if first_number > second_number:
    first_number, second_number = second_number, first_number

sum_of_numbers = 0
for number in range(first_number, second_number + 1):
    sum_of_numbers += number

print(f"A soma dos numeros no intervalo é: {sum_of_numbers}")

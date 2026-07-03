# Exercicio 4
# Escreva um programa que solicite duas vezes a entrada de um numero inteiro.
# O programa deve exibir a soma dos inteiros dentro do intervalo entre
# esses dois numeros, incluindo os dois limites.
#
# Exemplo:
# Se o usuario informar 10 e 15, a soma deve ser 75.
# 10 + 11 + 12 + 13 + 14 + 15 = 75

first_number = int(input("Digite o primeiro numero inteiro: "))
second_number = int(input("Digite o segundo numero inteiro: "))

sum_of_numbers = 0
while first_number <= second_number:
    sum_of_numbers += first_number
    first_number += 1

print(f"A soma dos numeros no intervalo é: {sum_of_numbers}")

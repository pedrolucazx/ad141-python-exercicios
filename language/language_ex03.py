# Exercicio 3
# Escreva um programa que solicite duas vezes a entrada de um numero inteiro.
# O programa deve exibir o maior dos dois numeros.
# Se os numeros forem iguais, o programa deve indicar isso.

first_number = int(input("Digite o primeiro numero inteiro: "))
second_number = int(input("Digite o segundo numero inteiro: "))

if first_number > second_number:
    print(f"O maior numero é: {first_number}")
elif second_number > first_number:
    print(f"O maior numero é: {second_number}")
else:
    print("Os numeros são iguais.")

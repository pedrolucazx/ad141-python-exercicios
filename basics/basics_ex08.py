# Exercício 8
# Escreva um programa que peça ao utilizador, duas vezes, para introduzir um número.
# O primeiro número será a base e o segundo número será o expoente.
# Imprima o resultado da elevação da base ao expoente.

base = float(input("Digite a base: "))
exponent = float(input("Digite o expoente: "))

print(f"{base} elevado a {exponent} é igual a {base ** exponent}.")

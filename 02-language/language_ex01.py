# Exercicio 1
# Escreva um programa que solicite um numero da sorte.
# O programa deve exibir uma mensagem se o numero informado nao for um inteiro.

luck_number = input("Digite seu numero da sorte: ")
if not luck_number.isnumeric():
    print("O valor informado não é um número inteiro")

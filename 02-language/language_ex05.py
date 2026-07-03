# Exercicio 5
# Peca ao usuario para informar varios numeros em uma unica linha.
# Separe os numeros em uma lista.
# Escreva um laço que examine cada elemento da lista e exiba
# apenas os valores maiores que zero.

numbers = input("Digite varios numeros separados por espaco: ")
numbers_list = numbers.split()

for number in numbers_list:
    if float(number) > 0:
        print(number)

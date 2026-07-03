# Exercicio 2
# Escreva um programa que fique em loop pedindo para o usuario inserir um numero.
# Repita ate o usuario digitar a palavra "end".
#
# Use como base:
# prompt = "Enter a number (or the word 'end' to quit) "
# while True:
#     data = input(prompt)
#     if data == "end":
#         break
#     # Remainder of while loop goes here
#
# A cada iteracao, adicione o numero em uma lista.
# Antes do programa encerrar, imprima:
# 1) o conteudo da lista em uma linha
# 2) a soma dos elementos da lista na linha seguinte

numbers = []
amount = 0

while True:
    data = input("Digite um numero (ou a palavra 'end' para sair) ")
    if data == "end":
        break
    if not data.isdigit():
        print("Entrada invalida. Digite um numero ou 'end'.")
        continue

    numbers.append(int(data))
    amount += int(data)

print(numbers)
print(amount)

# Exercício 6
# Escreva um programa que solicite duas vezes a introdução de um número inteiro.
# Imprima o produto dos dois números.
# Quando isto funcionar corretamente, tente introduzir números com uma vírgula decimal.
# O que acontece? Porquê?
# ! ValueError: estamos usando a função int() para converter a entrada
# ! do usuário em um número inteiro. Quando o usuário insere um número
# ! com uma vírgula decimal, como "3,14", a função int() não consegue
# ! converter essa string em um número inteiro, resultando em um erro.

first_number = int(input("Digite o primeiro número inteiro: "))
second_number = int(input("Digite o segundo número inteiro: "))

product = first_number * second_number
print(f"O produto dos dois números é: {product}")

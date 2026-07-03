# Exercicio 5
# Use um dicionario para mapear os digitos de 0 a 9 para as palavras:
# zero, one, two, three, four, five, six, seven, eight, nine.
#
# Depois, solicite que o usuario informe um numero.
# Exemplo: se o usuario digitar 1437, o programa deve imprimir:
# one four three seven.

digit_to_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero",
}

number = input("Digite um número: ")
for digit in number:
    print(digit_to_word[int(digit)])

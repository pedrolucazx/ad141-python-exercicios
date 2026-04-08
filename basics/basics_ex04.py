# Exercício 4
# Escreva um programa que peça ao usuário para digitar uma frase.
# O programa deve determinar e exibir as seguintes informações:
# O primeiro caractere da sequência de texto e o número de vezes que ele aparece na sequência.
# O último caractere da sequência de texto e o número de vezes que ele aparece na sequência.

phrase = input("Digite uma frase: ")
first_char = phrase[0]
last_char = phrase[-1]

first_char_count = phrase.count(first_char)
last_char_count = phrase.count(last_char)

print(
    f"O primeiro caractere é '{first_char}' e aparece {first_char_count} vezes na frase."
)
print(f"O último caractere é '{last_char}' e aparece {last_char_count} vezes na frase.")

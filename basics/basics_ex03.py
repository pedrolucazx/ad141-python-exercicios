# Exercício 3
# Escreva um programa que receba uma sequência de caracteres do usuário.
# Determine e imprima as seguintes informações sobre a sequência:
# Ela termina com um ponto?
# Ela contém apenas caracteres alfabéticos?
# Existe um 'x' na sequência?
# Crie e imprima uma nova sequência em que todas as ocorrências de 'e' tenham sido alteradas para 'E'.

user_input = input("Digite uma sequência de caracteres: ")
ends_with_dot = user_input.endswith(".")
is_alpha = user_input.isalpha()
contains_x = user_input.find("x") != -1
new_sequence = user_input.replace("e", "E")

print(f"Termina com um ponto? {'Sim' if ends_with_dot else 'Não'}")
print(f"Contém apenas caracteres alfabéticos? {'Sim' if is_alpha else 'Não'}")
print(f"Existe um 'x' na sequência? {'Sim' if contains_x else 'Não'}")
print(f"Nova sequência com 'e' alterado para 'E': {new_sequence}")

# Exercício 2
# Escreva um programa que solicite duas vezes a entrada de texto do usuário.
# A primeira entrada deve ser o nome.
# A segunda entrada deve ser o sobrenome.
# O programa deve exibir o nome completo em uma linha e as iniciais da pessoa na segunda linha.

first_name = input("Digite seu nome: ")
last_name = input("Digite seu sobrenome: ")

print(f"Nome completo: {first_name} {last_name}")
print(f"Iniciais: {first_name[0]} {last_name[0]}.")

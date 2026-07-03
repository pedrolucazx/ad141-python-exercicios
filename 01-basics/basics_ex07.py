# Exercício 7
# Escreva um programa que peça ao usuário para introduzir uma cadeia
# de caracteres e, em seguida, peça-lhe para introduzir um número.
# O programa deve criar e apresentar uma nova cadeia de caracteres
# utilizando o operador de repetição com a cadeia de caracteres e o número.
# Por exemplo, se a cadeia de caracteres for «hello» e o número for 3,
# então deve ser apresentado «hellohellohello».

user_string = input("Digite uma palavra ou frase: ")
user_number = int(input("Digite um número: "))

print(user_string * user_number)

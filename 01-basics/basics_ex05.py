# Exercício 5
# Escreva uma aplicação que solicite a introdução do raio de um círculo.
# Guarde o valor introduzido pelo usuário numa variável.
# Calcule e apresente a área do círculo cujo raio foi introduzido.
# A fórmula para a área de um círculo é πr² (pi vezes o quadrado do raio).
# Utilize 3,14159 para pi.

PI = 3.14159
radius = float(input("Digite o raio do círculo: "))
area = PI * (radius**2)
print(f"A área do círculo é {area:.2f}")

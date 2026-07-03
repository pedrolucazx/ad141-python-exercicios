# Exercicio 2
# Escreva uma list comprehension para criar uma lista de tuplas
# de x e o fatorial de x, para os numeros de 5 a 10 inclusive.
# Use math.factorial().

import math

result = [(x, math.factorial(x)) for x in range(5, 11)]

for x, fat in result:
    print(f"{x}! = {fat}")
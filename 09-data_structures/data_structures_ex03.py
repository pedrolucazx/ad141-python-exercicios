# Exercicio 3
# Escreva uma dictionary comprehension que gera um dicionario
# de numeros e seus fatoriais no intervalo (1, 10).
# Usando esse dicionario, multiplique 6 fatorial por 5 fatorial.

import math

factorias = {x: math.factorial(x) for x in range(1, 10)}

print("Fatoriais:", factorias)

resultado = factorias[6] * factorias[5]
print(f"6! * 5! = {factorias[6]} * {factorias[5]} = {resultado}")
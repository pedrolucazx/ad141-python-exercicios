# Exercicio 1
# Escreva list comprehensions para produzir as seguintes listas:
#
# (a) Uma lista com os elementos 0, 1, 2, 3, 4, ..., 99
# (b) Uma lista a partir da comprehension anterior com os valores
#     que sao divisiveis por 5

a = [x for x in range(100)]
b = [x for x in a if x % 5 == 0]

print("Lista 0..99:", a)
print("Divisiveis por 5:", b)
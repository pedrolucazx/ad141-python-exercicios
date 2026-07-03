# Exercicio 1
# Dadas as listas abaixo:
# first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
#
# Crie uma nova lista concatenando os elementos de first e second pelo indice.
# Ao final, a lista deve conter:
# ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
result = []

for i in range(7):
    result.append(first[i] + second[i])

print(result)

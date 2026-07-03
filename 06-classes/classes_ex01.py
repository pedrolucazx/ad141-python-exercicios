#!/usr/bin/env python3
# Exercicio 1
# Crie uma classe chamada Person.
#
# Cada Person deve ter um nome, uma idade e um genero.
# Alem de getters e setters para os atributos acima,
# a classe Person deve ter um metodo __init__() e um metodo __str__().

from person import Person

p1 = Person("Michael", 45, "M")
print(p1)